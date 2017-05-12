from modeltranslation.translator import register, TranslationOptions

from backend.backend.core.models import Program


@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('title',)
