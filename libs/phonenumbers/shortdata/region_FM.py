"""Auto-generated file, do not edit by hand. FM metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_FM = PhoneMetadata(id='FM', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='3\\d{5}|9\\d{2}', possible_number_pattern='\\d{3}(?:\\d{3})?'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='320221|911', possible_number_pattern='\\d{3}(?:\\d{3})?', example_number='911'),
    short_code=PhoneNumberDesc(national_number_pattern='320221|911', possible_number_pattern='\\d{3}(?:\\d{3})?', example_number='911'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    carrier_specific=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
