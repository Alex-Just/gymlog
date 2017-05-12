from haystack import indexes

from backend.backend.core.models import Exercise


class ProgramIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    docid = indexes.CharField(model_attr='id')

    def get_model(self):
        return Program
