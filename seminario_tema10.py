


# i code this with a friend in the first semester of college.

# you can access the repository where we worked here: https://github.com/luisgustavocarmelo/trabalho-ap1s1

 
 
Opcoes_do_Menu_Principal = ['Alunos', 'Cursos', 'Matrículas', 'Relatórios', 'SAIR']
Opcoes_do_Submenu = ['Listar todos', 'Listar um', 'Incluir novo registro', 'Alterar', 'Excluir']

arquivoAlunos = 'alunos.csv'
arquivoCursos = 'cursos.csv'
arquivoMatriculas = 'matriculas.csv'

nomenclaturaDosDadosDosAlunos = ['CPF', 'Nome', 'Data de nascimento', 'Sexo', 'e-mail', 'Telefone']
nomenclaturaDosDadosDosCursos = ['Código', 'Descrição', 'Carga', 'Preço']
nomenclaturaDeMatriculas = ['CPF', 'Código', 'Data de início', 'Data de término', 'Desconto']

alunos =    [
                [123, 'Antonio', '01/01/2001', 'Masculino', ['a@a.com', 'aa@aa.com'], ['11 99999 9999', '11 1111 1111']],
                [456, 'Bruna', '02/02/2002', 'Feminino', ['b@b.com'], ['22 99999 9999']],
                [789, 'Carlos', '03/03/2003', 'Masculino', ['c@c.com'], ['33 99999 9999']]
            ]

cursos =    [
                [234, 'Curso 1', 11, '111.00'], 
                [456, 'Curso 2', 22, '222.00']
            ]

matriculas =    [
                    ['123', '456', '01/01/2001', '11/11/2001', '10.0'],
                    ['123', '234', '01/02/2001', '11/12/2001', '20.0'],
                    ['789', '234', '01/01/2001', '11/12/2001', '30.0'],
                    ['456', '456', '02/02/2002', '22/02/2002', '40.0']
                ]

def menu(nomenclaturaDosDadosDosAlunos, nomenclaturaDosDadosDosCursos, alunos, cursos, matriculas):
    print('Menu de opções:')
    menuEscolhido = imprimeOpcoesESolicitaEscolha(Opcoes_do_Menu_Principal)

    if menuEscolhido != 5 and menuEscolhido != 4:
        
        subMenuEscolhido = imprimeOpcoesESolicitaEscolha(Opcoes_do_Submenu)

        #Menu Alunos
        if menuEscolhido == 1:
            if subMenuEscolhido == 1:
                listarTodosElementos(alunos,nomenclaturaDosDadosDosAlunos,'aluno')
            elif subMenuEscolhido == 2:
                listarUmElemento(alunos, nomenclaturaDosDadosDosAlunos, 'aluno')
            elif subMenuEscolhido == 3:
                incluirAluno(alunos, arquivoAlunos)
            elif subMenuEscolhido == 4:
                alterarDados(nomenclaturaDosDadosDosAlunos, alunos, 'aluno')    
            elif subMenuEscolhido == 5:
                deletarElemento(alunos, 'aluno')
        
        #Cursos
        elif menuEscolhido == 2:
            if subMenuEscolhido ==1:
                listarTodosElementos(cursos, nomenclaturaDosDadosDosCursos, 'curso')
            elif subMenuEscolhido == 2:
                listarUmElemento(cursos, nomenclaturaDosDadosDosCursos, 'curso')
            elif subMenuEscolhido == 3:                
                incluirCurso(cursos, arquivoCursos)
            elif subMenuEscolhido == 4:
                alterarDados(nomenclaturaDosDadosDosCursos, cursos, 'curso')
            elif subMenuEscolhido == 5:
                deletarElemento(cursos, 'curso')
        
        #Matrículas
        elif menuEscolhido == 3:
            if subMenuEscolhido ==1:
                listarTodosElementos(matriculas, nomenclaturaDeMatriculas, 'matricula')
            elif subMenuEscolhido == 2:
                listarUmElemento(matriculas, nomenclaturaDeMatriculas, 'matricula')    
            elif subMenuEscolhido == 3:
               incluirMatricula(alunos, cursos, matriculas, arquivoMatriculas)
            elif subMenuEscolhido == 4:
                alterarDados(nomenclaturaDeMatriculas, matriculas, 'matricula')   
            elif subMenuEscolhido == 5:
                deletarElemento(matriculas, 'matricula')
            

    #Relatórios
    elif menuEscolhido == 4:
        menuDeRelatorios(cursos,alunos,matriculas)
    #Sair
    else:
        print('Até logo! :)')

def menuDeRelatorios(cursos,alunos,matriculas):
    destacaTexto('Relatórios disponíveis:')
    print('1 - Mostrar o nome do curso, o CPF, o nome e os e-mails de todos os alunos que cursaram determinado curso cujo código você irá fonecer.')
    print('2 - Mostrar os dados de todos os cursos oferecidos entre as datas X e Y, onde as datas você irá fornecer.')
    print('3 - Mostrar os dados de todos os cursos realizados por determinado aluno, cujo CPF você irá fornecer.')

    destacaTexto('')
    escolha = int(input('Qual relatório você deseja consultar?'))

    if escolha == 1:
        RelatorioA(cursos,alunos,matriculas)
    if escolha == 2:
        relatorioB(cursos, matriculas)
    if escolha == 3:
        relatorioC(matriculas, cursos, alunos)

#Mostrar o nome do curso, o CPF, o nome e os e-mails de todos os alunos que cursaram determinado curso cujo código você irá fonecer.
def RelatorioA(cursos,alunos,matriculas):
    codigo = int(input('Digite o código do curso que deseja consultar: '))

    cursoEncontrado = False
    tamanhoCursos = len(cursos)
    for i in range(tamanhoCursos):
        if cursos[i][0] == codigo:
            destacaTexto('Listagem de alunos do curso: ', cursos[i][1])
            cursoEncontrado = True

    #se o curso não foi encontrado, avisa o usuário.
    if cursoEncontrado == False:
        destacaTexto('Este código de curso não foi encontrado. Tente novamente.')
        continuaOuSai()
    #se o curso foi encontrado, exibe as informações:
    else:
        exibeInformacoesRelatorioA(matriculas, alunos, codigo)

def exibeInformacoesRelatorioA(matriculas, alunos, codigo):
    contador = 1
    tamanhoMatriculas = len(matriculas)
    for j in range(tamanhoMatriculas):
        if int(matriculas[j][1]) == codigo:

            print()
            destacaTexto('Aluno ', contador)
            print('CPF:', matriculas[j][0])
            
            #percorre lista dos alunos, para ter o nome e e-mails de cada aluno encontrado.
            tamanhoAlunos = len(alunos)
            for k in range(tamanhoAlunos):
                if int(matriculas[j][0]) == alunos[k][0]:

                    print('Nome:', alunos[k][1])
                    print('E-mail(s):', transformaListaEmString(alunos[k][4], ', '))
                    contador += 1

    continuaOuSai()

def comparaDatas(dtInicialFornecida, dtFinalFornecida, dtInicialCurso, dtFinalCurso):
    
    dtInicialFornecida = dtInicialFornecida.split('/')
    dtFinalFornecida = dtFinalFornecida.split('/')

    dtInicialCurso = dtInicialCurso.split('/')
    dtFinalCurso = dtFinalCurso.split('/')

    #confere data inicial
    dataInicialConfere = False
    if dtInicialFornecida[2] >= dtInicialCurso[2]: #compara ano
        if dtInicialFornecida[1] >= dtInicialCurso[1]: #compara mês
            if dtInicialFornecida[0] >= dtInicialCurso[0]: #compara dia
                dataInicialConfere = True
        
    if dataInicialConfere == False:
        return False
    else:
        #confere data final
        dataFinalConfere = False
        if dtFinalFornecida[2] <= dtFinalCurso[2]: #compara ano
            if dtFinalFornecida[1] <= dtFinalCurso[1]: #compara mês
                if dtFinalFornecida[0] <= dtFinalCurso[0]: #compara dia
                    dataFinalConfere = True
        
    if dataFinalConfere:
        return True

# Mostrar os dados de todos os cursos oferecidos entre as datas X e Y, onde as datas devem ser fornecidas pelo usuário
def relatorioB(cursos, matriculas):

    dtInicial = input('Digite a data inicial (DD/MM/AAAA): ')
    dtFinal = input('Digite a data final (DD/MM/AAAA): ')

    cursosNestaData = []
    tamanhoMatricula = len(matriculas)
    for i in range(tamanhoMatricula):
        if (comparaDatas(dtInicial, dtFinal, matriculas[i][2], matriculas[i][3]) == True) and matriculas[i][1] not in cursosNestaData:
            cursosNestaData.append(matriculas[i][1])
    
    #se não encontrou nenhum curso, avisa o usuário.
    if len(cursosNestaData) == 0:
        destacaTexto('Não existe nenhum curso compreendido entre as datas fornecidas. Por favor, tente novamente')
        continuaOuSai()
    #se o curso foi encontrado, exibe as informações:
    else:
        exibeInformacoesRelatorioB(cursos, cursosNestaData)

def exibeInformacoesRelatorioB(cursos, cursosNestaData):

    tamanhoCursos = len(cursos)
    cursoEncontrado = False
    for i in range(tamanhoCursos):
        if str(cursos[i][0]) in cursosNestaData:
            destacaTexto('CURSO: ', cursos[i][1])
            print('Código:', cursos[i][0])
            print('Carga:', cursos[i][2])
            print('Preço:', cursos[i][3])
            print()
            cursoEncontrado = True

    if cursoEncontrado == False:
        print('Não encontrou curso. Tente novamente.')

    continuaOuSai()

# Mostrar os dados de todos os cursos realizados por determinado aluno, cujo CPF será fornecido pelo usuário.
def relatorioC(matriculas, cursos, alunos):
    cpfDoAluno = input('Digite o CPF (sem pontos ou traços): ')

    #valida se cpf já existe
    if (verificaNovoCodigo(int(cpfDoAluno), alunos)) == False:
        cursosDoAluno = {}

        tamanho = len(matriculas)
        matriz = []
        for i in range(tamanho):
            if matriculas[i][0] == cpfDoAluno:
                matriz.append(matriculas[i][1])
        
        cursosDoAluno[cpfDoAluno] = matriz
        # print(cursosDoAluno)

        exibeInformacoesRelatorioC(cursosDoAluno, cursos)

    else:
        destacaTexto('CPF não encontrado. Tente novamente.')
        continuaOuSai()

def exibeInformacoesRelatorioC(cursosDoAluno, cursos):

    cursoEncontrado = False
    for i in cursosDoAluno.values():
        tamanhoCursos = len(cursos)
        cursoEncontrado = False
        for j in range(tamanhoCursos):
            if str(cursos[j][0]) in i:
                destacaTexto('CURSO: ', cursos[j][1])
                print('Código:', cursos[j][0])
                print('Carga:', cursos[j][2])
                print('Preço:', cursos[j][3])
                print()
                cursoEncontrado = True

    if cursoEncontrado == False:
        print('Este aluno não está matriculado em nenhum curso. Tente novamente.')
    
    continuaOuSai()

def salvarMatrizNoArquivo(matriz, nomeArquivo):
    arquivo = open(nomeArquivo,'w')
    quantidadeDeLinhas = len(matriz)
    for i in range(quantidadeDeLinhas):
        lista = matriz[i]
        linha = ""
        for elemento in lista:
            linha = linha + str(elemento) + ';'
        linha = linha[:len(linha)-1]
        linha = linha + '\n'
        #print(linha) #debug
        arquivo.write(linha)
    arquivo.close()

def qualArquivo(tipo):
    if tipo == 'aluno':
        arquivo = arquivoAlunos
    elif tipo == 'curso':
        arquivo = arquivoCursos
    elif tipo == 'matricula':
        arquivo = arquivoMatriculas

    return arquivo

def alterarDados(nomenclatura, matriz, tipo): 
    print('Digite o', nomenclatura[0], 'do(a) ', tipo, ' a ser alterado(a):' )   
    codigo = int(input())

    confimacaoMatricula = True

    #confirmaçao de matricula
    if tipo == 'matricula':
            print('Digite o código do curso registrado nessa matricula:')
            codigoCurso = (input())
            confimacaoMatricula = verificaSeMatriculaJaExiste(codigo, codigoCurso, matriculas)


    if (verificaNovoCodigo(codigo,matriz)) or (confimacaoMatricula == False):
        print('O ', nomenclatura[0],' digitado nao existe no banco de dados.')

    #alteração de informaçoes
    if verificaNovoCodigo(codigo,matriz) == False and confimacaoMatricula:
        indiceDoCodigoNaLista = retornaIndiceDoCodigo(codigo,matriz)  
        print('O que voce deseja alterar?')
        escolhaDoUsuario = imprimeOpcoesESolicitaEscolha(nomenclatura)
        
        if tipo =='matricula' or  (escolhaDoUsuario > 0 and escolhaDoUsuario < 5):            
            print('Digite uma nova informação para ', nomenclatura[escolhaDoUsuario - 1], ': ')
            novaInformacao = input()
            matriz[indiceDoCodigoNaLista][escolhaDoUsuario-1] = novaInformacao
            destacaTexto("Informação alterada")
            
        elif tipo != 'matricula' and escolhaDoUsuario > 4 and escolhaDoUsuario < 7:
            if len(matriz[indiceDoCodigoNaLista][escolhaDoUsuario-1]) == 0:
                print('Digite uma nova informação para ', nomenclatura[escolhaDoUsuario - 1], ': ')
                novaInformacao = input()
                matriz[indiceDoCodigoNaLista][escolhaDoUsuario-1] = novaInformacao
                destacaTexto("Informação alterada")
            else:
                #alteração de email ou telefone
                #caso exista mais de um elemento, deve perguntar qual elemento quer alterar
                if len(matriz[indiceDoCodigoNaLista][escolhaDoUsuario-1]) > 1:
                    tamanho = len(matriz[indiceDoCodigoNaLista][escolhaDoUsuario-1])
                    for i in range(tamanho):
                        print(nomenclatura[escolhaDoUsuario-1], i+1, ': ',matriz[indiceDoCodigoNaLista][escolhaDoUsuario-1][i])

                    print('Qual ',nomenclatura[escolhaDoUsuario - 1],'você quer alterar?')    
                    qual_alterar = int(input())
                    if (qual_alterar-1) > len(matriz[indiceDoCodigoNaLista][escolhaDoUsuario-1]):
                        print("Essa opção não existe")
                    else:
                        print('Digite uma nova informação para ', nomenclatura[escolhaDoUsuario - 1], ': ')
                        novaInformacao = input()
                        matriz[indiceDoCodigoNaLista][escolhaDoUsuario-1][qual_alterar-1] = novaInformacao
                        destacaTexto("Informação alterada")
                
                #caso não seja lista, é uma alteração comum
                else:
                    print('Digite uma nova informação para ', nomenclatura[escolhaDoUsuario - 1], ': ')
                    novaInformacao = input()
                    matriz[indiceDoCodigoNaLista][escolhaDoUsuario-1] = novaInformacao
                    destacaTexto("Informação alterada")

        #imprime os dados alterados
        imprimeUmElemento (matriz,indiceDoCodigoNaLista,nomenclatura)

        
    #altera o arquivo
    arquivo = qualArquivo(tipo)
    salvarMatrizNoArquivo(matriz, arquivo)

    continuaOuSai() 

def retornaIndiceDoCodigo(codigoReferencia, lista):
    for i in range (len(lista)):
        if (codigoReferencia == int(lista[i][0])):
            local = i
    return local        

def imprimeOpcoesESolicitaEscolha(lista):

    for i in range(len(lista)):
        print(i+1,lista[i])
         
    opcaoEscolhida = int(input('Digite o número do opção desejada: '))

    if opcaoEscolhida < 0 or (opcaoEscolhida) > len(lista):
        destacaTexto('Esta opção não existe.')
        continuaOuSai()
    else:
        destacaTexto('Você escolheu a opção', lista[opcaoEscolhida - 1]) #informa opção escolhida
        return opcaoEscolhida

def listarTodosElementos(lista, listaReferencia, tipo):

    if (len(lista)) < 1:
        destacaTexto('Não foram encontrados registros.')
        continuaOuSai()
    else:
        destacaTexto('RESULTADO:')

        for i in range (len(lista)):
            if tipo == 'aluno':
                destacaTexto('DADOS DO ALUNO:', lista[i][1])
            elif tipo == 'curso':
                destacaTexto('DADOS DO CURSO:', lista[i][1])
            elif tipo == 'matricula':
                destacaTexto('DADOS DA MATRICULA:', lista[i][1])
                

            imprimeUmElemento(lista, i , listaReferencia )     
          
    continuaOuSai()

def listarUmElemento(lista, listaReferencia, tipo):

    if tipo == 'aluno' or tipo == 'matricula':
        codigo = int(input('Digite o CPF do aluno: '))
    elif tipo =='curso':
        codigo = int(input('Digite o Código do curso: '))  
    else:
        codigo = ''    
    
    codigo_existente_na_lista = False  
    for i in range(len(lista)):    
        if int(lista[i][0]) == codigo:
            codigo_existente_na_lista = True  
            destacaTexto('RESULTADO:')          
            imprimeUmElemento (lista, i , listaReferencia ) 
        
    if codigo_existente_na_lista == False:
        destacaTexto('Não encontrado. Tente novamente.')
        continuaOuSai()

    continuaOuSai()

def imprimeUmElemento (lista,posicaoNaLista,nomenclatura):    
    tamanho = len(lista[posicaoNaLista])
    for a in range (tamanho):
        if type(lista[posicaoNaLista][a]) is not list:
            print(nomenclatura[a],': ', lista[posicaoNaLista][a])
        else:
            print(nomenclatura[a],': ', transformaListaEmString((lista[posicaoNaLista][a]), ', '))

def incluiEmailOuTelefone(tipo):

    frase = 'Digite a quantidade de ' + tipo + 's que deseja inserir: '
    quantidade = int(input(frase))

    lista = []
    contador = 0
    while quantidade > 0:
        frase = 'Digite o ' + str(contador + 1) + 'º ' + tipo + ': '
        elemento = input(frase)
        lista.append(elemento)
        contador += 1
        quantidade -= 1

    return lista

#transforma lista em string, em que cada elemento da lista é separado por um delimitador recebido como parâmetro.
def transformaListaEmString(lista, delimitador):
    if type(lista) is list:
        tamanho = len(lista)
        string = ''

        # se houver apenas um, apenas transforma em string.
        if tamanho <= 1:
            string = str(lista[0])
        # se houver mais de um, separa pelo delimitador.
        else:
            for i in range(tamanho):
                if i == 0:
                    string = str(lista[0])
                else:
                    string = string + delimitador + str(lista[i])
    else:
        string = str(lista)

    return string

def incluirAluno(alunos, arquivo):
    
    print('Insira os dados abaixo:')
    cpf = int(input('CPF (sem pontos ou traços): '))
              
    #valida se cpf já existe
    if (verificaNovoCodigo(cpf, alunos)):
        nome = input('Nome completo: ')
        dtNascimento = input('Data de nascimento (MM/DD/AAAA): ')
        sexo = input('Sexo (M/F): ')
        email = incluiEmailOuTelefone('e-mail')
        telefone = incluiEmailOuTelefone('telefone')


        emailComDelimitador = transformaListaEmString(email, ',')
        telefoneComDelimitador = transformaListaEmString(telefone, ',')
        insereNoArquivoENaMatriz([cpf, nome, dtNascimento, sexo, emailComDelimitador, telefoneComDelimitador], alunos, arquivo)

        destacaTexto('Aluno incluído com sucesso!')
    else:
        destacaTexto('Este CPF já existe. Por favor, tente novamente.')

    continuaOuSai()

def verificaSeMatriculaJaExiste(cpf, codigo, matriculas):
    tamanho = len(matriculas)
    confirmacao = False
    for i in range(tamanho):
        if str(matriculas[i][0]) == str(cpf) and str(matriculas[i][1]) == str(codigo):
            confirmacao = True

    return confirmacao

def incluirMatricula(alunos, cursos, matriculas, arquivo):
    destacaTexto('Você irá fazer uma MATRÍCULA!')
    print('Insira os dados abaixo:')

    cpf = int(input('CPF (sem pontos ou traços): '))
    cpfNaoExiste = verificaNovoCodigo(cpf, alunos)
    if cpfNaoExiste:
        destacaTexto('Não há nenhum aluno vinculado à este CPF. Comece novamente.')
    else:
        codigo = int(input('Código do Curso (somente numeros): '))
        if verificaNovoCodigo(codigo, cursos):
            destacaTexto('Não há nenhum curso vinculado à este código. Comece novamente')

        else:
            #Se a matrícula já foi feita, não é possível fazê-la novamente.
            matriculaJaExiste = verificaSeMatriculaJaExiste(cpf, codigo, matriculas)
            if matriculaJaExiste:
                destacaTexto('Esta matrícula já foi efetuada anteriormente. Comece novamente.')

            #se a matrícula é nova, prossegue o cadastro.
            else:
                dtInicio = input('Data de início (DD/MM/AAAA): ')
                dtTermino = input('Data de término (DD/MM/AAAA): ')
                desconto = float(input('Desconto (em %) '))

                #monta o dicionário.
                dicionario = {}
                tupla = (cpf, codigo)
                lista = [dtInicio, dtTermino, desconto]
                dicionario[tupla] = lista
                print('O dicionário criado é ', dicionario)

                insereDicionarioNoArquivoENaMatriz(dicionario, matriculas, arquivo)

                destacaTexto('Matrícula incluída com sucesso!')

    continuaOuSai()

def insereDicionarioNoArquivoENaMatriz(dicionario, matriculas, arquivo):

    #insere no arquivo
    linha = ''
    for chave in dicionario.keys():
        #insere as chaves (código e cpf)
        linha = str(chave[0]) + ';' + str(chave[1])

        #insere os valores (dtInicio, dtTermino e desconto)
        linha = linha + ';' + str(dicionario[chave][0]) + ';' + str(dicionario[chave][1]) + ';' + str(dicionario[chave][2]) + '\n'

    # print('linha que será inserida no arquivo', linha)   
    arquivo = open (arquivo, 'a')
    arquivo.write(linha)
    arquivo.close

    #transforma linha em lista, para inserir na matriz
    linha = linha.replace('\n', '')
    linha = linha.split(';')
    
    #insere na matriz
    matriculas.append(linha)

def insereNoArquivoENaMatriz(listaElementos, matriz, arquivo):
    lista = []
    linha = ''
    tamanho = len(listaElementos)
    for i in range(tamanho):
        linha = linha + str(listaElementos[i]) + ';'
        lista.append(listaElementos[i])
    #no final, insere o \n
    linha = linha + '\n'

    #insere no arquivo
    arquivo = open (arquivo, 'a')
    arquivo.write(linha)
    arquivo.close

    #insere na matriz
    matriz.append(lista)

def incluirCurso(cursos, arquivo):
    print('Insira os dados abaixo:')
    codigo = int(input('Código do Curso (somente numeros): '))
              
    #valida se codigo já existe
    if (verificaNovoCodigo(codigo, cursos)):
        descricao = input('Descrição: ')
        cargaHoraria = int(input('Carga horária (somente números): '))
        preco = float(input('Preço: '))

        insereNoArquivoENaMatriz([codigo, descricao, cargaHoraria, preco], cursos, arquivo)

        destacaTexto('Curso incluído com sucesso!')
    else:
        destacaTexto('Este código de curso já existe. Por favor, tente novamente.')

    continuaOuSai()

def verificaNovoCodigo(codigo, lista):
    novoCodigo = True
    
    # verifica CPF ou código.
    for i in range (len(lista)):
        if (codigo == int(lista[i][0])):
            novoCodigo = False

    return novoCodigo

def deletarElemento(lista, tipo):
    destacaTexto('Confirme os dados do cadastro que deseja excluir')

    if tipo == 'aluno':
        cpf = int(input('CPF (sem pontos ou traços): '))
        dtNascimento = input('Data de nascimento (MM/DD/AAAA): ')
        confereEDeleta(lista, cpf, dtNascimento, tipo)
    elif tipo == 'curso':
        codigo = int(input('Código do Curso (somente numeros): '))
        cargaHoraria = int(input('Carga Horaria (somente números): '))
        confereEDeleta(lista, codigo, cargaHoraria, tipo)
    elif tipo == 'matricula':
        cpf = int(input('CPF do aluno (somente numeros): '))
        dataInicio = str(input('Data de inicio: '))
        confereEDeleta(lista, cpf, dataInicio, tipo)
    
    continuaOuSai()

def nomenclaturaDados(tipo):
    if tipo == 'aluno':
        stringChave = 'CPF'
        stringConferencia = 'Data de nascimento'
    elif tipo == 'curso':
        stringChave = 'Código do curso'
        stringConferencia = 'Carga Horária'
    elif tipo == 'matricula':
        stringChave = 'CPF'
        stringConferencia = 'Data Inicio'
    else:
        stringChave = ''
        stringConferencia = ''

    return stringChave, stringConferencia

def confereEDeleta(lista, chave, conferencia, tipo):

    stringChave, stringConferencia = nomenclaturaDados(tipo)

    cadastroExiste = False
    chaveExiste = False
    i = 0
    while (cadastroExiste == False and i <len(lista)):
        if int(lista[i][0]) == chave:
            chaveExiste = True
            if str(lista[i][2]) == str(conferencia):
                print('O seguinte ', tipo, ' terá seu cadastro deletado:', lista[i][1])
                del lista[i]
                destacaTexto('Cadastro deletado com sucesso!')
                cadastroExiste = True

                #deleta tambem do arquivo
                arquivo = qualArquivo(tipo)
                salvarMatrizNoArquivo(lista,arquivo)
        i += 1
    
    if (chaveExiste == False):
        destacaTexto('Não foi encontrado o ', stringChave)
    elif (cadastroExiste == False):
            print(stringChave, ' e ', stringConferencia, 'não coincidem. Não foi possível excluir')

def destacaTexto(texto, variavel = ''):
    print('----------------')
    print(texto, variavel)
    print('----------------')

def continuaOuSai():
    print('_____________________________')
    escolha = input('Digite S para sair ou aperte ENTER para continuar. ')

    #se escolheu continuar, exibe menu
    if escolha.lower() != 's':
        menu(nomenclaturaDosDadosDosAlunos, nomenclaturaDosDadosDosCursos, alunos, cursos, matriculas)

#para facilitar os testes, os arquivos inicialmente são gerados a partir das variáveis globais da memória.
def carregaDadosIniciaisParaArquivo(nomeArquivo, matriz):
    arquivo = open(nomeArquivo,'w')
    # arquivo.write(cabecalho+'\n')
    qtddLinhas = len(matriz)
    for i in range(qtddLinhas):
        lista = matriz[i]
        linha = ""
        for elemento in lista:
            linha = linha + transformaListaEmString(elemento, ',')+";"
        linha = linha[:len(linha)-1]
        linha = linha+ '\n'
        #print(linha) #debug
        arquivo.write(linha)
    arquivo.close()

def main(): 
    #para facilitar os testes, os arquivos inicialmente são gerados a partir das variáveis globais da memória.
    carregaDadosIniciaisParaArquivo(arquivoAlunos, alunos)
    carregaDadosIniciaisParaArquivo(arquivoCursos, cursos)
    carregaDadosIniciaisParaArquivo(arquivoMatriculas, matriculas)

    menu(nomenclaturaDosDadosDosAlunos, nomenclaturaDosDadosDosCursos, alunos, cursos, matriculas)

main()