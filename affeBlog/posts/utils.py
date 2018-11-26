from django.utils.text import slugify

import random
import string

'''
generate a random string to produce the unique slug 

'''


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
'''
recursively generate the slug url 
'''


def unique_slug_generator(instance, new_slug=None):
    # all the code is to test if the new_slug is already used
    # if used generate a new one and test that, if not used just
    # use this current slug to be the final slug
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug