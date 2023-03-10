fn_in = './movies.txt'
fn_out = './movies_clean.txt'

allowed_chars = """!"$&'()*+,-./ 0123456789:;?@[]abcdefghijklmnopqrstuvwxyz}"""

movies = open(fn_in, 'r').readlines()

with open(fn_out, 'w') as f_out:
    for movie in movies:
        movie = movie.lower()
        movie = ''.join([a for a in movie if a in allowed_chars])
        f_out.write(movie + '\n')
