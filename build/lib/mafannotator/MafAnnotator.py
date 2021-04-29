import argparse
from mafannotator.AnnotatorCore import *

def annotate(input, output, token):
    setoncokbapitoken(token)
    processalterationevents(input, output, "", "",{}, False, None, None)
