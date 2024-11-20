from um import count

def main():
    #test
    test_UM_allCaps()

def test_UM_allCaps():
    assert count("um ms;qam;mqe um knslknflnum kjjsnknkncum um skNLNSDLNUM") == 3
    assert count("UM NJSNLJNSLUM UM ADNLNDLNCLUM umnljijj jnjljnum efdcumscac") == 2
    assert count("lllnlnum um ak;kamslc um jisajnclasn um kasmclaknmsum um") == 4
    assert count("nlnnln um mum UMM UM.") == 2
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2

