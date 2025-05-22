import os
import csv
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Perfumes_boticario:
    Lily_Le_Parfum:str
    Malbec_gold:str
    Her_Code_Touch:str
    Egeo_Blue:str
    Elysee_Blanc:str


lista_perfumes = []

def esperar_enter():
    input("\n PRESSIONE ENTER PARA CONTINUAR")

def mostar_menu():