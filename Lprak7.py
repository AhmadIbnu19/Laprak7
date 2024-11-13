def akhiran(number):
            if 10 <= number % 100 <= 10:
                return 'th'
            else:
                sisa_bagi = number % 10
                if sisa_bagi == 1:
                    return 'st'
                elif sisa_bagi == 2:
                    return 'nd'
                elif sisa_bagi == 3:
                    return 'rd'
                else:
                    return 'th'

def UrutanAngka(number):
    hasil_akhiran = akhiran(number)
    return f'{number}{hasil_akhiran}' 

def isian():
 print('Selamat datang di program yang di buat oleh')
 print('\tAhmad Ibnu Batutah')
 while True:
    number = int(input('Masukan bilangan (0 untuk stop): '))
    if number == 0:
          print('Terima kasih sudah menggunakan program ini :)')
          break
    else:
          print(f'Input\t: {number}\nOutput\t: {UrutanAngka(number)}')
isian()