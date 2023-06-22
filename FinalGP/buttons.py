from  string import ascii_lowercase, ascii_uppercase, digits, punctuation

from enum import Enum

class Characters(Enum):
    Button_AZ = ascii_uppercase
    Button_az = ascii_lowercase
    Button_09 = digits
    Button_Special = punctuation

CHARACTER_NUMBER = {
    'Button_AZ': len(Characters.Button_AZ.value),
    'Button_az': len(Characters.Button_az.value),
    'Button_Special': len(Characters.Button_Special.value),
    'Button_09': len(Characters.Button_09.value)
}

GENERATE_PASSWORD = (
    'btn_refresh', 'Button_az','Button_AZ','Button_09','Button_Special'
)
