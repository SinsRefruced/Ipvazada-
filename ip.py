import requests
import sys
from colorama import Fore, Style

while True:
    print('\n')  # Melhorando a formatação

    print(f'{Fore.RED}██╗      ██████╗ ███████╗████████╗     ██╗     {Style.RESET_ALL}')
    print(f'{Fore.RED}██║     ██╔═══██╗██╔════╝╚══██╔══╝     ██║     {Style.RESET_ALL}')
    print(f'{Fore.RED}██║     ██║   ██║███████╗   ██║        ██║     {Style.RESET_ALL}')
    print(f'{Fore.RED}██║     ██║   ██║╚════██║   ██║        ██║     {Style.RESET_ALL}')
    print(f'{Fore.RED}███████╗╚██████╔╝███████║   ██║        ███████╗{Style.RESET_ALL}')
    print(f'{Fore.RED}╚══════╝ ╚═════╝ ╚══════╝   ╚═╝        ╚══════╝{Style.RESET_ALL}')
    print(f'{Fore.BLUE}                           by Sins {Style.RESET_ALL}')

    print('\nEscolha uma opção:')
    print(f'{Fore.BLUE}[1] Informações de IP{Style.RESET_ALL}')
    print(f'{Fore.BLUE}[2] Instruções de investigação{Style.RESET_ALL}')
    print(f'{Fore.BLUE}[3] Fechar{Style.RESET_ALL}')

    i = input('- ')

    if i == '1':
        try:
            ip = input('Digite o IP (Ex: 192.168.0.1): ')
            r = requests.get(f'https://ipinfo.io/{ip}/json', timeout=5)
            r.raise_for_status()  # Garante que um erro HTTP seja capturado

            d = r.json()
            print(f'\n{Fore.GREEN}== INFORMAÇÕES DO IP =={Style.RESET_ALL}')
            print('IP:', d.get('ip', 'Informação não disponível'))
            print('Cidade:', d.get('city', 'Informação não disponível'))
            print('Região:', d.get('region', 'Informação não disponível'))
            print('País:', d.get('country', 'Informação não disponível'))
            print('Nome do País:', d.get('country_name', 'Informação não disponível'))
            print('Timezone:', d.get('timezone', 'Informação não disponível'))
            print('Localização:', d.get('loc', 'Informação não disponível'))
            print('Organização:', d.get('org', 'Informação não disponível'))
            print('Hostname:', d.get('hostname', 'Informação não disponível'))
            print('Postal:', d.get('postal', 'Informação não disponível'))
            print('Anycast:', d.get('anycast', 'Informação não disponível'))
            print('Versão da API:', d.get('version', 'Informação não disponível'))

        except requests.exceptions.RequestException as e:
            print(f'{Fore.RED}Erro ao buscar informações do IP:{Style.RESET_ALL}', e)
    
    elif i == '2':
        print(f'\n{Fore.YELLOW}== INSTRUÇÕES DE INVESTIGAÇÃO =={Style.RESET_ALL}')
        print('Deseja investigar mais um endereço IP? Esses comandos vão te ajudar.')
        print('\nNMAP - Ferramenta de Investigação:')
        print(f'{Fore.GREEN}Linux:{Style.RESET_ALL} sudo apt-get install nmap')
        print(f'{Fore.RED}Termux:{Style.RESET_ALL} pkg install nmap')
        print(f'{Fore.BLUE}Windows:{Style.RESET_ALL} Disponível em nmap.org')
        print('\nComandos básicos:')
        print('→ `nmap -sV <IP>` - Descobrir serviços e versões nas portas abertas')
        print('→ `nmap -O <IP>` - Verificar o sistema operacional do dispositivo')
        print('→ `nmap -A <IP>` - Fazer uma varredura agressiva')
        print(f'{Fore.RED}⚠️ Lembre-se: qualquer ação realizada é de sua responsabilidade.{Style.RESET_ALL}')
    
    elif i == '3':
        print(f'\n{Fore.RED}Fechando...{Style.RESET_ALL}')
        sys.exit()
    
    else:
        print(f'{Fore.RED}Comando inválido, tente novamente.{Style.RESET_ALL}')