import re
import sys
import time

def remove_comments(code: str, language: str) -> str:
    """
    Author by dimasbp 
    recode izin dulu ler
    ig : dmzby_
    fb : dimasdev
    
    """
    patterns = {
        'dart': r'(\/\/.*?$|\/\*[\s\S]*?\*\/)', 
        'html': r'<!--[\s\S]*?-->',                  
        'css': r'\/\*[\s\S]*?\*\/',               
        'php': r'(\/\/.*?$|\/\*[\s\S]*?\*\/|#.*?$)', 
        'python': r'(#.*?$|\'\'\'[\s\S]*?\'\'\'|\"\"\"[\s\S]*?\"\"\")', 
        'cpp': r'(\/\/.*?$|\/\*[\s\S]*?\*\/)', 
        'java': r'(\/\/.*?$|\/\*[\s\S]*?\*\/)', 
        'csharp': r'(\/\/.*?$|\/\*[\s\S]*?\*\/)', 
    }

    if language not in patterns:
        raise ValueError(f"Unsupported language: {language}")

    pattern = patterns[language]
    cleaned_code = re.sub(pattern, '', code, flags=re.MULTILINE)
    return cleaned_code

def show_loading(message: str):
    """Display a loading bar animation with a custom message."""
    for i in range(20):  
        sys.stdout.write('\r' + message + ' [' + '#' * i + ' ' * (20 - i) + ']')
        sys.stdout.flush()
        time.sleep(0.1)  
    sys.stdout.write('\n')  

if __name__ == "__main__":
    print("\n========================")
    print("[#] AUTHOR   : LEOXSEC")
    print("[#] GITHUB   : dimasbp-dev")
    print("")
    print("[!] Menghapus komentar dari file kode sumber untuk beberapa bahasa pemrograman  HTML, CSS, PHP, Dart, Python, C++, Java, dan C#.")
    print("========================")
    print("1. HTML")
    print("2. CSS")
    print("3. PHP")
    print("4. Dart")
    print("5. Python")
    print("6. C++")
    print("7. Java")
    print("8. C#")
    print("========================\n")

    choice = input("\u2794 Enter your choice : ")
    languages = {
        "1": "html",
        "2": "css",
        "3": "php",
        "4": "dart",
        "5": "python",
        "6": "cpp",
        "7": "java",
        "8": "csharp",
    }

    if choice not in languages:
        print("\n\u274C Invalid choice. Please try again.")
    else:
        print("\n\u23F3 Processing your choice...\n")
        show_loading("Loading language selection")  

        language = languages[choice]
        print(f"\n\u270D Please provide the path to your {language.upper()} file.")

      
        show_loading("Please wait while the program prepares")

        file_path = input(f"\u2794 Path to {language.upper()} file: ")

        try:
            
            print("\n\u23F3 Processing your file... please wait.")
            show_loading("Processing file")

            with open(file_path, "r") as file:
                code = file.read()

            cleaned_code = remove_comments(code, language)

            output_path = file_path.replace(".html", "_cleaned.html")\
                                   .replace(".css", "_cleaned.css")\
                                   .replace(".php", "_cleaned.php")\
                                   .replace(".dart", "_cleaned.dart")\
                                   .replace(".py", "_cleaned.py")\
                                   .replace(".cpp", "_cleaned.cpp")\
                                   .replace(".java", "_cleaned.java")\
                                   .replace(".cs", "_cleaned.cs")

            with open(output_path, "w") as output_file:
                output_file.write(cleaned_code)

            print(f"\n\u2705 Comments removed. Cleaned code saved to: {output_path}\n")
        except FileNotFoundError:
            print("\n\u274C File not found. Please check the file path and try again.")
        except Exception as e:
            print(f"\n\u274C An error occurred: {e}")
