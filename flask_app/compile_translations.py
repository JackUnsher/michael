import os
import subprocess
from pathlib import Path

def compile_translations():
    """Компилирует файлы переводов .po в .mo"""
    print("Компиляция файлов переводов...")
    
    # Путь к директории с переводами
    translations_dir = Path(__file__).parent / 'translations'
    
    # Перебираем все языки
    for lang_dir in translations_dir.iterdir():
        if lang_dir.is_dir():
            lang = lang_dir.name
            po_file = lang_dir / 'LC_MESSAGES' / 'messages.po'
            mo_file = lang_dir / 'LC_MESSAGES' / 'messages.mo'
            
            if po_file.exists():
                print(f"Компиляция {lang}...")
                
                # Используем msgfmt для компиляции .po в .mo
                try:
                    from babel.messages.mofile import write_mo
                    from babel.messages.pofile import read_po
                    
                    with open(po_file, 'rb') as po_file_handle:
                        catalog = read_po(po_file_handle)
                    
                    with open(mo_file, 'wb') as mo_file_handle:
                        write_mo(mo_file_handle, catalog)
                    
                    print(f"Файл {mo_file} успешно создан.")
                except Exception as e:
                    print(f"Ошибка при компиляции {lang}: {e}")
            else:
                print(f"Файл {po_file} не найден.")
    
    print("Компиляция завершена.")

if __name__ == "__main__":
    compile_translations()
