"""
Implemente uma classe ConversorTemperatura que converte temperaturas de Celsius para Fahrenheit. 
A classe deve incluir um método chamado celsius_para_fahrenheit que realiza o cálculo de conversão. 
A fórmula para converter de Celsius para Fahrenheit é:

Fahrenheit = (Celsius x 95) + 32Fahrenheit = (Celsius x 59) + 32

Você também deverá criar uma instância do conversor e utilizar essa instância para realizar a conversão.


"""
class Converter_temperatura:
    def celsius_para_fahrenheit(self, celsius):
        self.celsius = celsius
        fahrenheit = 1.8 * celsius + 32
        return fahrenheit
    
celsius = int(input('Digite a temperatura em celsius: '))

conversor = Converter_temperatura()
fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(f'A temperatura {celsius}° equivale a {fahrenheit}F.')

