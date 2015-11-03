from django.core.exceptions import ValidationError
from django.conf import settings

def file_allowed_types(object_file):
    """
    object_file adalah parameter bertype object dari 
    class InMemoryUploadedFile. class ini ada di 
    package django.core.files.uploadedfile. class ini juga
    turunan dari class UploadedFile. class UploadedFile merupakan
    turunan dari class File dari package django.core.files. jadi 
    apapun yang bisa dilakukan pada File juga bisa dilakukan oleh
    class InMemoryUploadedFile.

        --------------------
        File (base class)
        --------------------
                |
                |    EXTENDS
                |
        --------------------
        UploadedFile
        --------------------
                *
               /|\
                |    EXTENDS
                |
        --------------------
        InMemoryUploadedFile
        -------------------- 
    """

    print(object_file.content_type)
    pesan_error = "File '{}' tidak di dukung dalam sistem ini !"
    if object_file.content_type not in settings.MORPYN_FILE_ALLOW:
        raise ValidationError(pesan_error.format(object_file.name))
    

def file_allowed_size(object_file):
    # batas 5242880 kb atau 5mb
    size = object_file.size
    batas = settings.MORPYN_FILE_SIZE_MAX
    pesan_error = "Ukuran File '{}' melebihi batas maksimal !"
    if size > batas:
        raise ValidationError(pesan_error.format(object_file.name))

# deprecated
def password_allowed_size(value):
    pesan_error = "Password '{}' harus diatas 5 dan kurang dari 8 karaketer"
    if len(value) > 8 or len(value) < 5:
        raise ValidationError(pesan_error.format("*"*len(value)))