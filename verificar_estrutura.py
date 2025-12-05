import os
import sys
import importlib.util

def check_path(path, is_file=True):
    """Verifica se um arquivo ou diretório existe."""
    exists = os.path.isfile(path) if is_file else os.path.isdir(path)
    symbol = "✅" if exists else "❌"
    print(f"{symbol} {path}")
    return exists

def check_import(module_name):
    """Tenta importar um módulo para testar os __init__.py."""
    try:
        importlib.import_module(module_name)
        print(f"✅ Importação '{module_name}' funcionou!")
        return True
    except ImportError as e:
        print(f"❌ Falha ao importar '{module_name}': {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado em '{module_name}': {e}")
        return False

def main():
    print("--- INICIANDO AUDITORIA DO BEAL-PIPELINE ---\n")
    
    all_good = True
    
    # 1. Verificando Estrutura de Pastas e Arquivos Críticos
    print("[1] Verificando Arquivos Essenciais:")
    files_to_check = [
        ("README.md", True),
        ("pyproject.toml", True),
        (".gitignore", True),
        ("spectral_proof_2025", False),
        ("spectral_proof_2025/core", False),
        ("spectral_proof_2025/core/metrics.py", True),
        ("spectral_proof_2025/simulation", False),
        ("spectral_proof_2025/visualization", False),
        ("legacy_proof", False),
    ]
    
    for path, is_file in files_to_check:
        if not check_path(path, is_file):
            all_good = False

    print("\n[2] Verificando Configuração de Pacotes (__init__.py):")
    # Adiciona o diretório atual ao path para permitir imports
    sys.path.append(os.getcwd())
    
    modules_to_test = [
        "spectral_proof_2025",
        "spectral_proof_2025.core",
        "spectral_proof_2025.simulation",
        "spectral_proof_2025.visualization"
    ]
    
    for mod in modules_to_test:
        if not check_import(mod):
            all_good = False

    print("\n" + "="*40)
    if all_good:
        print("🎉 PARABÉNS! A estrutura do repositório está PERFEITA.")
        print("Você pode fazer o push para o GitHub com segurança.")
    else:
        print("⚠️ ATENÇÃO: Encontramos problemas (veja os '❌' acima).")
        print("Verifique se você criou todos os arquivos __init__.py corretamente.")
    print("="*40)

if __name__ == "__main__":
    main()