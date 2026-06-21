class Muestra:
    def __init__(self, id_muestra, paciente, volumen_ml, tipo_analisis):
        # Se guardan los atributos básicos de la muestra
        self.id = id_muestra
        self.paciente = paciente
        self.volumen = volumen_ml
        self.tipo = tipo_analisis

    def clasificar(self):
        # Se hace la clasificación basada en los umbrales de meta.txt
        # El límite inferior es inclusivo (>=) y el superior exclusivo (<)
        if self.volumen < 13.91:
            return "Micro"
        elif 13.91 <= self.volumen < 50.81:
            return "Pequeña"
        elif 50.81 <= self.volumen < 149.34:
            return "Mediana"
        elif 149.34 <= self.volumen < 347.01:
            return "Grande"
        else:
            return "Extra grande"

    def __str__(self):
        # Representación legible para el usuario
        return f"{self.id} | {self.paciente} | {self.volumen}ml"

    def __repr__(self):
        # Representación técnica para depuración
        return f"Muestra(id='{self.id}', valor={self.volumen}, clase='{self.clasificar()}')"