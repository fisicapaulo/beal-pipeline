# spectral_proof_2025/run_pipeline_e.py
from pipeline_e.pipeline_e import pipeline_E

def main():
    # Exemplo simples (coprimos). Ajuste A,B,C conforme queira testar.
    A, B, C = 5, 7, 3
    # Ajuste as constantes para valores consistentes com sua teoria (Apêndice E).
    delta = 0.2
    alpha_Q = 10.0
    C0 = 100.0

    result = pipeline_E(A, B, C, delta=delta, alpha_Q=alpha_Q, C0=C0, verbose=True)
    print("\n=== Pipeline E: Resultado ===")
    for k, v in result.items():
        if k != "survivors":
            print(f"{k}: {v}")
    print(f"survivors (até {min(10,len(result['survivors']))}): {result['survivors'][:10]}")

if __name__ == "__main__":
    main()
