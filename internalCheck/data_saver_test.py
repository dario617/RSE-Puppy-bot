import data_saver

test_result = {
    'measure_time' : "1-12-3 12:00:00",
    'temp1_cur' : 0.1,
    'temp1_max' : 0.1,
    'temp2_cur' : 0.1,
    'temp2_max' : 0.1,
    'temp3_cur' : 0.1,
    'temp3_max' : 0.1,
    'temp4_cur' : 0.1,
    'temp4_max' : 0.1,
    'mem_dsp' : '300G',
    'mem_use' : '300G',
    'dsk_dsp' : '200G',
    'disk_use' : '200G',
    'CPU' : 0.99
}

test_input = {
    'Date' : {
        'year' : 1,
        'month': "dec",
        'day': 3,
        'time': "12:00:00"
    },
    'Temp4' : {
        'actual' : 0.1,
        'max' : 0.1
    },
    'Temp7' : {
        'actual' : 0.1,
        'max' : 0.1
    },
    'Temp10' : {
        'actual' : 0.1,
        'max' : 0.1
    },
    'Temp13' : {
        'actual' : 0.1,
        'max' : 0.1
    },
    'Memory' : {
        'disponible' : '300G',
        'usage' : '300G'
    },
    'Disk' : {
        'disponible' : '200G',
        'usage' : '200G'
    },
    'CPU' : 0.99
}

def test_():
    resultIs = data_saver.dic_to_data(test_input)
    assert resultIs == test_result
