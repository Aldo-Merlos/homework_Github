import ROOT

hist = ROOT.TH1F("h_gaus", "Gaussian Histogram;Value;Entries", 100, -5, 5)

random = ROOT.TRandom3(0)

for i in range(20000):
    value = random.Gaus(0, 1.5)
    hist.Fill(value)

print("Number of entries:", hist.GetEntries())
print("Mean:", hist.GetMean())
print("Standard deviation:", hist.GetStdDev())
