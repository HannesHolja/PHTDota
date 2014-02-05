#-------------------------------------------------------------------------------
# Name:        pelaajat
# Purpose:
#
# Author:      Hannes Holja
#
# Created:     05.02.2014
# Copyright:   (c) Hannes Holja 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Pelaajat:

    def __init__(nimi, ika, kansalaisuus, kieli, voittohavio, taitotaso):
        self.__nimi = nimi
        self.__ika = ika
        self.__kansalaisuus = kansalaisuus
        self.__kieli = kieli
        self.__voittohavio = voittohavio
        self.__taitotaso = taitotaso

    def get__nimi(self):
        return self.__nimi
    def set__nimi(self):
        self.__nimi = nimi

    def get__ika(self):
        return self.__ika
    def set__ika(self):
        self.__ika = ika
    def get__kansalaisuus(self):
        return self.__kansalaisuus
    def set__kansalaisuus(self):
        self.__kansalaisuus = kansalaisuus
    def get__kieli(self):
        return self.__kieli
    def set__kieli(self):
        self.__kieli = kieli
    def get__voittohavio(self):
        return self.__voittohavio
    def set__voittohavio(self):
        self.__voittohavio = voittohavio

    def get__taitotaso(self):
        return self.__taitotaso

    def set__taitotaso(self):
        self.__taitotaso

    #def __str__(self)
