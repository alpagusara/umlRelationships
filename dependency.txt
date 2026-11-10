class FormatConverter:
    def to_uppercase(self, text: str) -> str:
        return text.upper()

class Logger:
    # Logger depends on FormatConverter only for this operation
    def log_message(self, message: str, converter: FormatConverter):
        formatted = converter.to_uppercase(message)
        print(f"LOG: {formatted}")

# Usage
logger = Logger()
tool = FormatConverter()
logger.log_message("system error", tool)
          
