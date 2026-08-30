import os

from pypdf import PdfReader

#读取文件
def load_documents(folder_path):
    documents = []


    for filename in os.listdir(folder_path):
        file_path = os.path.join(
            folder_path,
            filename
        )


        if filename.endswith(".txt"):

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                documents.append(
                    {
                        "filename": filename,
                        "content": content
                    }
                )

        #读取PDF文件
        elif filename.endswith(".pdf"):
            reader = PdfReader(file_path)

            content = ""
            for page in reader.pages:
                text = page.extract_text()


                if text:
                    content += text


            documents.append(
                {
                    "filename": filename,
                    "content": content
                }
            )
            

    return documents


