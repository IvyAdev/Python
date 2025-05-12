class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"❌ Error: The file '{self.filename}' does not exist.")
            return None
        except PermissionError:
            print(f"❌ Error: You do not have permission to read '{self.filename}'.")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return None

    def write_file(self, content, new_filename):
        try:
            with open(new_filename, 'w') as file:
                file.write(content)
            print(f"✅ Modified content written to '{new_filename}'")
        except Exception as e:
            print(f"❌ Failed to write to '{new_filename}': {e}")

    def modify_content(self, content):
        # Modify content here (example: convert to uppercase)
        return content.upper()

    def process_file(self):
        content = self.read_file()
        if content is not None:
            modified_content = self.modify_content(content)
            new_filename = f"modified_{self.filename}"
            self.write_file(modified_content, new_filename)


def main():
    filename = input("Enter the name of the file to read: ")
    file_handler = FileHandler(filename)
    file_handler.process_file()


if __name__ == "__main__":
    main()
