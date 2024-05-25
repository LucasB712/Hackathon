#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {

    print('''   
████████╗██╗░░░██╗░█████╗░░█████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░░█████╗░
╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗██╔══██╗
░░░██║░░░██║░░░██║██║░░╚═╝██║░░██║██╔████╔██║███████║░░░██║░░░██║██║░░╚═╝███████║
░░░██║░░░██║░░░██║██║░░██╗██║░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██╗██╔══██║
░░░██║░░░╚██████╔╝╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░░██║
░░░╚═╝░░░░╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝   ''')

    
    srand(time(0)); // Seed para números aleatórios
    
    int operacao = rand() % 4; // Escolhe aleatoriamente a operação (0 para adição, 1 para subtração, 2 para multiplicação, 3 para divisão)
    
    int num1, num2, resposta, resultado;

    switch(operacao) {
        case 0: // Adição
            num1 = rand() % 10 + 1; // Número aleatório entre 1 e 10
            num2 = rand() % 10 + 1; // Número aleatório entre 1 e 10
            resultado = num1 + num2;
            cout << "Quanto é " << num1 << " + " << num2 << "?" << endl;
            break;
        case 1: // Subtração
            num1 = rand() % 10 + 1; // Número aleatório entre 1 e 10
            num2 = rand() % 10 + 1; // Número aleatório entre 1 e 10
            resultado = num1 - num2;
            cout << "Quanto é " << num1 << " - " << num2 << "?" << endl;
            break;
        case 2: // Multiplicação
            num1 = rand() % 5 + 1; // Número aleatório entre 1 e 5
            num2 = rand() % 5 + 1; // Número aleatório entre 1 e 5
            resultado = num1 * num2;
            cout << "Quanto é " << num1 << " * " << num2 << "?" << endl;
            break;
        case 3: // Divisão
            num1 = rand() % 10 + 1; // Número aleatório entre 1 e 10
            num2 = rand() % 5 + 1; // Número aleatório entre 1 e 5
            // Garante que a divisão seja exata
            num1 = resultado = num1 * num2;
            cout << "Quanto é " << num1 << " / " << num2 << "?" << endl;
            break;
    }

    cin >> resposta;

    if (resposta == resultado) {
        cout << "Correto! Parabéns!" << endl;
    } else {
        cout << "Incorreto. A resposta correta é " << resultado << "." << endl;
    }

    return 0;
}
