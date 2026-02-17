def brew_chai(flavor):
    if flavor not in ["masala", "ginger" , "elachi"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")

brew_chai("mint")
      