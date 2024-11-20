def main():

    extension, name = (extract(input("what is the file name? ").strip().lower()))

    print(media_type(extension))



def extract(file):

    file = file[::-1] + '.'

    extension, name = file.split('.', 1)

    return(extension[::-1], name[::-1])

def media_type(ext):

    match ext:

        case "gif":
            return ("image/gif")

        case "jpg":
            return ("image/jpeg")

        case "jpeg":
            return ("image/jpeg")

        case "png":
            return ("image/png")

        case "pdf":
            return ("application/pdf")

        case "txt":
            return ("text/plain")

        case "zip":
            return ("application/zip")

        case _:
            return ("application/octet-stream")


if __name__ == "__main__":
    main()
