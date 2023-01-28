from django import forms
from django.forms import MultipleChoiceField, CheckboxSelectMultiple


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


FIELDS = [
    ("description", "description"),
    ("identifier", "identifier"),
    ("keywords", "keywords"),
    ("language", "language"),
    ("accessibilitySummary", "accessibilitySummary"),
    ("accountablePerson", "accountablePerson"),
    ("version", "version"),
    ("temporalCoverage", "temporalCoverage"),
    ("publisher", "publisher"),
    ("spatial", "spatial"),
    ("license", "license"),
    ("citation", "citation"),
    ("type/genre", "type/genre"),
    ("creator", "creator"),
    ("update/modification date", "update/modification date"),
    ("distribution", "distribution"),
    ("image", "image"),
    ("thumbnailUrl", "thumbnailUrl"),
    ("headline", "headline"),
    ("abstract", "abstract"),
    ("theme/category", "theme/category"),
    ("dateCreated", "dateCreated"),
    ("creditText", "creditText"),
    ("datePublished", "datePublished"),
    ("producer", "producer"),
    ("author", "author"),
    ("spatialCoverage", "spatialCoverage"),
    ("url", "url"),
    ("temporal", "temporal"),
    ("sponsor", "sponsor"),
    ("size", "size"),
    ("sdPublisher", "sdPublisher"),
    ("sdLicense", "sdLicense"),
    ("sameAs", "sameAs"),
    ("publication", "publication"),
    ("provider", "provider"),
    ("position", "position"),
    ("name", "name"),
    ("measurementTechnique", "measurementTechnique"),
    ("material", "material"),
    ("maintainer", "maintainer"),
    ("locationCreated", "locationCreated"),
    ("issn", "issn"),
    ("isPartOf", "isPartOf"),
    ("isBasedOn", "isBasedOn"),
    ("isAccessibleForFree", "isAccessibleForFree"),
    ("includedInDataCatalog", "includedInDataCatalog"),
    ("editor", "editor"),
    ("editEIDR", "editEIDR"),
    ("copyrightYear", "copyrightYear"),
    ("copyrightNotice", "copyrightNotice"),
    ("copyrightHolder", "copyrightHolder"),
    ("contributor", "contributor"),
    ("contentReferenceTime", "contentReferenceTime"),
    ("contentLocation", "contentLocation"),
    ("character", "character"),
    ("acquireLicensePage", "acquireLicensePage"),
    ("accessModeSufficient", "accessModeSufficient"),
    ("about", "about"),
    ("rights", "rights"),
    ("relation", "relation"),
    ("qualified relation", "qualified relation"),
    ("qualified attribution", "qualified attribution"),
    ("previous version", "previous version"),
    ("landing page", "landing page"),
    ("is referenced by", "is referenced by"),
    ("in series", "in series"),
    ("has version", "has version"),
    ("has policy", "has policy"),
    ("has current version", "has current version"),
    ("useConstraints", "useConstraints"),
    ("status", "status"),
    ("spatialRepresentationType", "spatialRepresentationType"),
    ("spatialRepresentationInfo", "spatialRepresentationInfo"),
    ("scope", "scope"),
    ("responsibleParty", "responsibleParty"),
    ("releasability", "releasability"),
    ("reference", "reference"),
    ("purpose", "purpose"),
    ("otherLocale", "otherLocale"),
    ("metadataProfile", "metadataProfile"),
    ("metadataLinkage", "metadataLinkage"),
    ("metadataIdentifier", "metadataIdentifier"),
    ("MD_LegalConstraints", "MD_LegalConstraints"),
    ("MD_Identification", "MD_Identification"),
    ("environmentDescription", "environmentDescription"),
    ("distributor", "distributor"),
    ("distributionInfo", "distributionInfo"),
    ("dataQualityInfo", "dataQualityInfo"),
    ("contentInfo", "contentInfo"),
    ("contact", "contact")
]


class SelectionForm(forms.Form):
    fields = MultipleChoiceField(
        required=False,
        widget=CheckboxSelectMultiple,
        choices=FIELDS,
    )
