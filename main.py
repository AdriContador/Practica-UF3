import functions as f
import literals as msg


def main():
   f_name = f.nomfitxer()
   header = f.fitxer_existent(f_name)
   if header == 1:
       sobreescriure = f.validate(msg.EXISTENT, 1, 2)
   if sobreescriure == 1:
       f.introregistres(f_name, 'w', header)
   else:
       f.introregistres(f_name, 'a', header)
if __name__ == '__main__':
   main()
