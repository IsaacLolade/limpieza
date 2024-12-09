import pandas as pd
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Proceso de limpieza de datos')
    parser.add_argument('--input', dest='input', required=True, help='Archivo de entrada')
    parser.add_argument('--output', dest='output', required=False, help='Archivo de salida')

    args = parser.parse_args()
    input_file = args.input
    output = args.output if args.output else "output.csv"

    if not input_file.lower().endswith(".csv"):
        raise ValueError("El archivo de entrada debe ser un archivo CSV")
    
    df = pd.read_csv(input_file, sep="\t")
    df = df.dropna()
    
    # Create the directory if it does not exist
    os.makedirs("limpios", exist_ok=True)
    
    df.to_csv(f"limpios/{output}", index=False, sep="\t")
    print("Proceso de limpieza finalizado")
    
if __name__ == "__main__":
    main()