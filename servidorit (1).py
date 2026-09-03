from datetime import datetime
import socket
import random
uzwMZVCZzmKRFnMTQusVlSjNLrzNsIdn = [
    "La vida es aquello que te sucede mientras estás ocupado haciendo otros planes. - John Lennon",
    "El único modo de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
    "No cuentes los días, haz que los días cuenten. - Muhammad Ali",
    "La imaginación es más importante que el conocimiento. - Albert Einstein",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día. - Robert Collier",
    "La mejor manera de predecir el futuro es crearlo. - Peter Drucker",
    "No hay caminos para la paz; la paz es el camino. - Mahatma Gandhi",
    "La felicidad no es algo hecho. Proviene de tus propias acciones. - Dalai Lama",
    "El mayor riesgo es no tomar ninguno. - Mark Zuckerberg",
    "La educación es el arma más poderosa que puedes usar para cambiar el mundo. - Nelson Mandela",
    "No dejes que el miedo te detenga. - Walt Disney",
    "El fracaso es solo la oportunidad de comenzar de nuevo, de forma más inteligente. - Henry Ford",
    "La suerte favorece a la mente preparada. - Louis Pasteur",
    "Haz lo que puedas, con lo que tengas, donde estés. - Theodore Roosevelt",
    "La vida es corta, sonríe mientras aún tienes dientes. - Anónimo",
    "El que no arriesga no gana. - Proverbio",
    "El tiempo es oro. - Proverbio",
    "El conocimiento es poder. - Francis Bacon",
    "La perseverancia es la clave del éxito. - Charles Chaplin",
    "Nunca es tarde para aprender. - Proverbio",
    "El amor mueve el mundo. - Virgilio",
    "La paciencia todo lo alcanza. - Santa Teresa de Jesús",
    "La esperanza es lo último que se pierde. - Proverbio",
    "El respeto al derecho ajeno es la paz. - Benito Juárez",
    "La libertad no es hacer lo que uno quiere, sino lo que debe. - Jean Paul Sartre",
    "El hombre nunca sabe de lo que es capaz hasta que lo intenta. - Charles Dickens",
    "La vida es un sueño. - Calderón de la Barca",
    "El que busca la verdad corre el riesgo de encontrarla. - Manuel Vicent",
    "La mejor venganza es el éxito masivo. - Frank Sinatra",
    "El arte de vencer se aprende en las derrotas. - Simón Bolívar",
    "La mente es como un paracaídas, solo funciona si se abre. - Albert Einstein",
    "El que tiene imaginación sin instrucción tiene alas sin pies. - Joseph Joubert",
    "La humildad es la verdadera llave del éxito. - Proverbio",
    "El optimismo es la fe que conduce al logro. - Helen Keller",
    "La disciplina es el puente entre metas y logros. - Jim Rohn",
    "El futuro pertenece a quienes creen en la belleza de sus sueños. - Eleanor Roosevelt",
    "La vida es una aventura, atrévete. - Teresa de Calcuta",
    "El talento gana partidos, pero el trabajo en equipo y la inteligencia ganan campeonatos. - Michael Jordan",
    "La creatividad es inteligencia divirtiéndose. - Albert Einstein",
    "El único límite a nuestros logros de mañana está en nuestras dudas de hoy. - Franklin D. Roosevelt",
    "La grandeza de una persona se mide por sus acciones. - Proverbio",
    "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. - Albert Schweitzer",
    "La mejor forma de empezar es dejar de hablar y comenzar a hacer. - Walt Disney",
    "El secreto de avanzar es comenzar. - Mark Twain",
    "La vida es demasiado importante como para tomarla en serio. - Oscar Wilde",
    "El que quiere interesar a los demás tiene que provocarlos. - Salvador Dalí",
    "La única forma de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
    "El que no vive para servir, no sirve para vivir. - Madre Teresa de Calcuta",
    "El éxito consiste en vencer el temor al fracaso. - Charles Chaplin"
]
def kUOwqVgRXVdBuTCbNvsARfkNHJrCPols():
    wRFjyDmdUaxDduOBiFzDroszfRgCEGOS = '0.0.0.0'
    dMloOwFOTKUulBQWvNqAAJYgScTIfrUL = 5001
    yNCoUagljZYdHkTAjnCjfNzuUgeBNwtN = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((wRFjyDmdUaxDduOBiFzDroszfRgCEGOS, dMloOwFOTKUulBQWvNqAAJYgScTIfrUL))
        s.listen()
        while True:
            gbMGicSozsSgvZtEFysFkosMDwbviiXb, ASAJWowkeqpWDPnTebhWMEiDhqrCEcnm = s.accept()
            with gbMGicSozsSgvZtEFysFkosMDwbviiXb:
                while True:
                    XCVgTdwDgyYbdYnndADEkzMjVWvGGFvA = gbMGicSozsSgvZtEFysFkosMDwbviiXb.recv(1024).decode('utf-8').strip()
                    if XCVgTdwDgyYbdYnndADEkzMjVWvGGFvA.lower() == "xazf":
                        NEiWLjDVtBhmwqAIcyCyTMXUjgOGOyKl = random.choice(uzwMZVCZzmKRFnMTQusVlSjNLrzNsIdn)
                        gbMGicSozsSgvZtEFysFkosMDwbviiXb.sendall(NEiWLjDVtBhmwqAIcyCyTMXUjgOGOyKl.encode('utf-8'))
                        gbMGicSozsSgvZtEFysFkosMDwbviiXb.sendall(b"\n")
                    if XCVgTdwDgyYbdYnndADEkzMjVWvGGFvA.lower() == "bb":
                        gbMGicSozsSgvZtEFysFkosMDwbviiXb.sendall(uzwMZVCZzmKRFnMTQusVlSjNLrzNsIdn[yNCoUagljZYdHkTAjnCjfNzuUgeBNwtN].encode('utf-8'))
                        gbMGicSozsSgvZtEFysFkosMDwbviiXb.sendall(b"\n")
                        yNCoUagljZYdHkTAjnCjfNzuUgeBNwtN += 2
                        yNCoUagljZYdHkTAjnCjfNzuUgeBNwtN %= len(uzwMZVCZzmKRFnMTQusVlSjNLrzNsIdn)
                    elif XCVgTdwDgyYbdYnndADEkzMjVWvGGFvA.lower() == "affhex":
                        kxCPivIpnUGwoEtVSUPgOvfjIImhOmgr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        gbMGicSozsSgvZtEFysFkosMDwbviiXb.sendall(b"\n")
                        gbMGicSozsSgvZtEFysFkosMDwbviiXb.sendall(kxCPivIpnUGwoEtVSUPgOvfjIImhOmgr.encode('utf-8'))
                    elif XCVgTdwDgyYbdYnndADEkzMjVWvGGFvA.lower() == "zzz":
                        gbMGicSozsSgvZtEFysFkosMDwbviiXb.sendall(b".")
                        break
                    else:
                        gbMGicSozsSgvZtEFysFkosMDwbviiXb.sendall(b"\n")
if __name__ == "__main__":
    kUOwqVgRXVdBuTCbNvsARfkNHJrCPols()