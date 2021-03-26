from django import forms
from .models import UploadFiles, TranscriptDetails, Review
from .choices import *


class UploadFilesForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True})
    )

    class Meta:
        model = UploadFiles
        fields = ('file',)


class TranscriptDetailsForm(forms.ModelForm):

    time_length = forms.ChoiceField(
        choices=TIME_LENGTH_CHOICES
    )
    text_format = forms.ChoiceField(
        choices=TEXT_FORMAT_CHOICES
    )
    number_of_speakers = forms.ChoiceField(
        choices=NUM_SPEAKER_CHOICES
    )
    timestamps = forms.ChoiceField(
        choices=TIMESTAMP_CHOICES
    )
    turn_around_time = forms.ChoiceField(
        choices=TAT_CHOICES
    )
    audio_quality = forms.ChoiceField(
        choices=AUDIO_QUAL_CHOICES
    )

    class Meta:
        model = TranscriptDetails
        fields = ['time_length', 'text_format', 'number_of_speakers', 'timestamps',
                  'turn_around_time', 'audio_quality']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
