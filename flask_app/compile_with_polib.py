import os
import polib
from pathlib import Path

def compile_translations():
    """Компилирует файлы переводов .po в .mo с использованием polib"""
    print("Компиляция файлов переводов...")
    
    # Путь к директории с переводами
    translations_dir = Path(__file__).parent / 'translations'
    
    # Перебираем все языки
    for lang_dir in translations_dir.iterdir():
        if lang_dir.is_dir():
            lang = lang_dir.name
            po_file_path = lang_dir / 'LC_MESSAGES' / 'messages.po'
            mo_file_path = lang_dir / 'LC_MESSAGES' / 'messages.mo'
            
            if po_file_path.exists():
                print(f"Компиляция {lang}...")
                
                try:
                    # Загружаем .po файл
                    po = polib.pofile(str(po_file_path))
                    
                    # Сохраняем как .mo файл
                    po.save_as_mofile(str(mo_file_path))
                    
                    print(f"Файл {mo_file_path} успешно создан.")
                except Exception as e:
                    print(f"Ошибка при компиляции {lang}: {e}")
            else:
                print(f"Файл {po_file_path} не найден.")
    
    print("Компиляция завершена.")

if __name__ == "__main__":
    compile_translations()
