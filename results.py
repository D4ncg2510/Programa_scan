import subprocess



def scan(hosts, ports, arguments, sudo=False):

    """
    Función para ejecutar un escaneo nmap.

    Argumentos pedidos al usuario:

        hosts (str): Direcciones IP de los hosts separadas por comas.
        ports (str): Puertos a escanear separados por comas.
        arguments (list): Lista de argumentos para nmap.
        sudo (bool, optional): Si se requieren privilegios de superusuario. Por default es False.

    Returns:
        None
    """
    command = ['nmap']
    if sudo:
        command.insert(0, 'sudo')  # Agrega 'sudo' al comando si se requieren privilegios de superusuario
    command.extend(['-p', ','.join(ports.split(','))])  # Agrega los puertos a escanear al comando
    command.extend(arguments)  # Agrega los argumentos al comando
    command.append(hosts)  # Agrega los hosts al comando
    try:

    # subprocess.run() se utiliza para ejecutar un comando en el sistema operativo
    # command es la lista de argumentos que se pasarán al comando
    # capture_output=True indica que se capture la salida estándar y la salida de error
    # text=True convierte la salida capturada en una cadena de texto
    # check=True hace que se lance una excepción si el comando devuelve un código de salida distinto de cero
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    # Si el comando se ejecuta correctamente, se imprime la salida estándar
    print(result.stdout)
except subprocess.CalledProcessError as e:
    # Si el comando devuelve un código de salida distinto de cero, se captura la excepción
    # e.stderr contiene la salida de error del comando
    print("Error:", e.stderr)

def main():

    hosts = input("Ingrese las direcciones IP de los hosts separadas por comas:")
    ports = input("Ingrese los puertos a escanear separados por comas:")
    arguments = []
    print("Ingrese los argumentos de nmap uno por uno ,escriba 'term' para terminar:")
    while True:
        arg = input("Argumento: ")
        if arg.lower() == 'term':
            break
        arguments.append(arg)
    sudo_input = input("¿Se requieren privilegios de superusuario? (si/no): ")
    sudo = sudo_input.lower() == 'si'
    scan(hosts, ports, arguments, sudo)
if __name__ == "__main__":
    main()

