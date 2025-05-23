from django.shortcuts import render
from .forms import contatoForm
from django.contrib import messages
#from django.core.mail import EmailMessage

def index(request):
    return render(request, "portfolio/index.html")

def product(request, id):
    return render(request, 'portfolio/pages/product-view.html', context={
        'nome':'Fábio Rodrigues de Moraes',
    })

def about(request):
    return render(request, 'portfolio/pages/about.html')

def curriculum(request):
    return render(request, 'portfolio/pages/curriculum.html')

def contact(request):
    form = contatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['name']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['subject']
            mensagem = form.cleaned_data['message']

            print('MENSAGEM ENVIADA COM SUCESSO!!!')
            print(f'Nome: {nome}')
            print(f'e-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensage: {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso!!!')

            #Configuração para enviar e-mail em produção
            #mail = EmailMessage(
            #    subject = assunto,
            #    body = nome + '\n' + email + '\n\n' + mensagem,
            #    from_email= 'no-reply@mail.com',
            #    to = ['fmoraes05@gmail.com', 'fmoraes05@outlook.com'],
            #)
            #mail.send()

            form = contatoForm()
        else:
            messages.error(request, 'Erro ao enviar a mensagem...')
            
    context = {
        'form': form,
    }
    return render(request, 'portfolio/pages/contact.html', context)