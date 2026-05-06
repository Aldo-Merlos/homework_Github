import ROOT

hist = ROOT.TH1F("h_gaus", "Gaussian Histogram;Value;Entries", 50, -5, 5)

random = ROOT.TRandom3(0)

for i in range(10000):
    value = random.Gaus(0, 1)
    hist.Fill(value)

print("Number of entries:", hist.GetEntries())
