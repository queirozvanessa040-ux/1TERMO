## Aula: Arquitetura IoT – Programação com Arduino, C++ e Python
## 1. Introdução à Arquitetura IoT

* Camada de Dispositivo: Sensores e atuadores coletam dados do ambiente físico.
* Camada de Rede: Gateways e protocolos transmitem os dados coletados.
* Camada de Aplicação: Servidores e nuvem processam e visualizam as informações.

------------------------------
## 2. O Ecossistema Arduino

* Hardware: Microcontroladores acessíveis com pinos de entrada/saída digitais e analógicos.
* Software (IDE): Ambiente de desenvolvimento para escrita e upload de código.
* Prototipagem: Facilidade de conexão com componentes eletrônicos sem solda.

------------------------------
## 3. Programação do Microcontrolador (C++)
O Arduino é programado em uma versão simplificada de C++. Todo código possui duas funções principais:

// Configuração inicial (executada uma vez)void setup() {
  pinMode(13, OUTPUT); // Define o pino 13 como saída digital
}
// Loop principal (executado continuamente)void loop() {
  digitalWrite(13, HIGH); // Liga o LED
  delay(1000);            // Aguarda 1 segundo
  digitalWrite(13, LOW);  // Desliga o LED
  delay(1000);            // Aguarda 1 segundo
}

## Conceitos Chave em C++ para IoT:

* Tipos de Dados: Uso de int, float, char e boolean para otimizar memória.
* Controle de Fluxo: Estruturas if/else e laços while/for condicionam ações dos sensores.
* Manipulação de Pinos: Funções digitalRead(), digitalWrite(), analogRead() e analogWrite().

------------------------------
## 4. Integração e Análise de Dados (Python)
O Python atua no lado do servidor ou gateway para coletar, processar e salvar os dados vindos do Arduino via comunicação serial.

import serialimport time
# Configura a porta serial (ajuste a porta conforme seu sistema)arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2) # Aguarda a conexão estabilizar
while True:
    if arduino.in_waiting > 0:
        # Lê a linha de dados enviada pelo Arduino
        dados = arduino.readline().decode('utf-8').rstrip()
        print(f"Dados do Sensor: {dados}")

## Conceitos Chave em Python para IoT:

* Biblioteca PySerial: Cria a ponte de comunicação direta com o hardware.
* Manipulação de Strings: Limpeza e formatação dos dados brutos recebidos.
* Armazenamento: Integração com bancos de dados ou exportação para arquivos CSV.

------------------------------
## 5. Prática Proposta: Monitor de Temperatura

   1. Arduino: Lê um sensor analógico e envia o valor via Serial.println().
   2. Python: Lê a porta serial e salva os dados em um arquivo de texto.

------------------------------
Para estruturar melhor o seu plano de ensino, informe:

* Qual é a duração total desta aula ou módulo?
* Os alunos usarão componentes físicos ou um simulador virtual (como o Tinkercad)?
* Qual o nível de conhecimento prévio da turma em programação?