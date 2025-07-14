import difflib
from data_dumps.occupation import occupations

class EktpReader:
    def __init__(self, ocr_data: list):
        # define global vars
        self.ocr_data = ocr_data
        self.result = None
        self.fields = {
            'nik': ['nik'],
            'name': ['nama', 'nama lengkap'],
            'birthplace_dob': ['tempat/tgl lahir', 'tempat', 'tgl', 'lahir'],
            'blood_type': ['gol darah', 'darah'],
            'gender': ['jenis kelamin', 'kelamin'],
            'address': ['alamat'],
            'rt_rw': ['rt/rw', 'rtrw', 'rtinw'],
            'village': ['kel/desa', 'kelurahan' 'desa'],
            'district': ['kecamatan'],
            'religion': ['agama'],
            'marital_status': ['status', 'status perkawinan'],
            'occupation': ['pekerjaan'],
            'citizenship': ['kewarganegaraan'],
        }
        self.marital_status = ["cerai mati", "cerai hidup", "belum kawin", "kawin"]
        self.religions = ["islam", "kristen (protestan)", "hindu", "budha", "katolik", "konghucu"]
        self.genders = ["laki-laki", "perempuan"]
        self.occupations = occupations

        # run process
        self.transform()

    def field_check(self, value: str):
        best_key = None
        best_score = 0
        treshold = 0.7

        for f in self.fields:
            for v in self.fields[f]:
                score = difflib.SequenceMatcher(None, value.lower(), v).ratio()
                if score > best_score and score >= treshold:
                    best_score = score
                    best_key = f
        return best_key
    
    def value_check(self, options: list, value: str, is_label: bool = False):
        if value is None:
            return None
        
        val = difflib.get_close_matches(value.lower(), options, n=1, cutoff=0.5)
        return val[0] if val is not None and len(val) > 0 else None

    def transform(self):
        if self.ocr_data is None:
            return

        # start transforming data
        extracted = {}
        active_field = None

        for i in range(len(self.ocr_data)-1, -1, -1):
            real_value = None
            text = self.ocr_data[i][1]
            if len(text) < 3:
                continue
            
            # case with split
            splitted = text.split(":")
            if len(splitted) > 1:
                text = splitted[0].replace(" ", "_")
                real_value = splitted[1].strip()

            # check valid field
            result = self.field_check(text)

            # appending data
            if real_value is not None:
                # case when field/label contain colon(:)
                extracted[result] = None

                # define options for checking valid value
                if result == "marital_status":
                    real_value = self.value_check(self.marital_status, real_value)
                
                # updating data
                if real_value is not None:
                    extracted[result] = real_value
                active_field = None
            elif result is not None:
                extracted[result] = None
                active_field = result
            elif active_field is not None:
                # define options for checking valid value
                options = []
                if active_field == "religion":
                    options = self.religions
                elif active_field == "gender":
                    options = self.genders
                elif active_field == "occupation":
                    options = self.occupations

                # cleaning text
                if len(options) > 0:
                    text = self.value_check(options, text)

                if text is not None and extracted[active_field] is None:
                    extracted[active_field] = text

        # updating global vars
        self.result = extracted