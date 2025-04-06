# Bad Interface
# class Machine:
#     def print(self): pass
#     def scan(self): pass
#     def fax(self): pass

# class OldPrinter(Machine):
#     def print(self): print("Printing...")
#     def scan(self): raise NotImplementedError()
#     def fax(self): raise NotImplementedError()

# Separate interfaces
class Printer:
    def print(self):
        raise NotImplementedError()

class Scanner:
    def scan(self):
        raise NotImplementedError()

class Faxer:
    def fax(self):
        raise NotImplementedError()

# A class that only prints
class SimplePrinter(Printer):
    def print(self):
        print("SimplePrinter: Printing document...")

# A class that can print and scan
class MultiFunctionPrinter(Printer, Scanner):
    def print(self):
        print("MultiFunctionPrinter: Printing document...")

    def scan(self):
        print("MultiFunctionPrinter: Scanning document...")

# A class that can print, scan, and fax
class AdvancedPrinter(Printer, Scanner, Faxer):
    def print(self):
        print("AdvancedPrinter: Printing document...")

    def scan(self):
        print("AdvancedPrinter: Scanning document...")

    def fax(self):
        print("AdvancedPrinter: Sending fax...")

if __name__ == "__main__":
    sp = SimplePrinter()
    sp.print()

    mfp = MultiFunctionPrinter()
    mfp.print()
    mfp.scan()

    ap = AdvancedPrinter()
    ap.print()
    ap.scan()
    ap.fax()
