import ET0735_Lab2.bmi as bmi

print("Test_bmi")
def test_bmi_normal_weight():
    result = bmi.calculate_bmi(weight=57, height=1.73)
    assert (result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(weight=300, height=1.73)
    assert (result == 1)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(weight=2, height=1.73)
    assert (result == -1)




