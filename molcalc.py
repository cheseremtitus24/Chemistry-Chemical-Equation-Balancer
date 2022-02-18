from molmass import Formula
import argparse

parser = argparse.ArgumentParser(
    description="Finds the Relative molar masses of Chemical Elements and Compounds. Example Run :  molcalc KHC8H4O4 "
                "--compute molarmass "
)
parser.add_argument("MolecularFormula", help="Molecular Formula e.g KHC8H4O4", type=str)
parser.add_argument("--compute",help="Find empirical or compute the Relative Molecular Mass ", choices=["molarmass", "empirical"], default="molarmass")
args = parser.parse_args()
# print(args)
compound = "{}".format(args.MolecularFormula)
f = Formula(compound)

if args.compute == "molarmass":
    print(compound, "has a relative molar mass of : ", f.mass, "grams")
else:
    print(compound, "has an Empirical Formula of : ",f.empirical)


