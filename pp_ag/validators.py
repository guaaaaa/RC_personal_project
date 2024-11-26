from django.core.exceptions import ValidationError

def validate_audio_size(value):
    filesize= value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")

def validate_video_size(value):
    filesize= value.size
    if filesize > 500000000:
        raise ValidationError("The maximum file size that can be uploaded is 500MB")