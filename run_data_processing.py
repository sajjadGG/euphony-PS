
import os
from sygus_parser import StrParser
from property_signatures import compute_property_sig
# from sygus_string_dsl import *
from utils import PATH_TO_STR_BENCHMARKS
import pickle
import json

def prop_sig_to_str(prop_sig):
    return ''.join(str(x) for x in prop_sig)

def str_to_prop_sig(str_in):
    return [int(s) for s in str_in]

def dict_to_jsonstr(dict_in):
    return json.dumps(dict_in)

def jsonstr_to_dict(jsonstr):
    return json.loads(jsonstr)

def inout_list_to_str(inout_list):
    return ','.join([dict_to_jsonstr(e) for e in inout_list])

def main():
    # con = sqlite3.connect("processed_data.db")
    # cur = con.cursor()
    # cur.execute("CREATE TABLE problem_input_output (problem, input_output_dicts)")
    # cur.execute("CREATE TABLE problem_property_signatures (problem, property_signatures)")
    '''
    problem -> (inout_dicts, prop_sigs)
    '''
    data_dict = {}



    benchmark_list = os.listdir(PATH_TO_STR_BENCHMARKS)
    for benchmark in benchmark_list:
        print("benchmark: ", benchmark)
        specification_parser = StrParser(benchmark)
        specifications = specification_parser.parse()
        # # Sygus grammar.
        # dsl_functions = [StrConcat, StrReplace, StrSubstr, StrIte, StrIntToStr, StrCharAt, StrLower, StrUpper, IntStrToInt,
        #                  IntPlus, IntMinus, IntLength, IntIteInt, IntIndexOf, IntFirstIndexOf, IntMultiply, IntModulo,
        #                  BoolEqual, BoolContain, BoolSuffixof, BoolPrefixof, BoolGreaterThan, BoolLessThan]

        string_variables = specifications[0]
        string_literals = specifications[1]
        integer_variables = specifications[2]
        integer_literals = specifications[3]
        input_output_examples = specifications[4]

        print("string_variables", string_variables)
        print("string_literals", string_literals)
        print("integer_variables", integer_variables)
        print("integer_literals", integer_literals)

        print("input_output_examples", input_output_examples)

        # compute property signature given each input-out example
        ps = compute_property_sig(input_output_dicts_list=input_output_examples,
                             string_variables_list=string_variables,
                             integer_variables_list=integer_variables)
        print(ps)
        print(len(ps))

        data_dict.update({os.path.splitext(benchmark)[0]:(input_output_examples, ps)})
        with open("processed_data.pickle", 'wb') as file:
            pickle.dump(data_dict, file)


        # '''
        # input_output table
        # problem -> input-output pairs
        # property_signature table
        # problem -> property signature
        # '''
        # cur.execute("INSERT INTO problem_input_output VALUES (\'"+benchmark+"\', \'"+inout_list_to_str(input_output_examples)+"\')")
        # cur.execute("INSERT INTO problem_property_signatures VALUES (\'"+benchmark+"\', \'"+prop_sig_to_str(ps)+"\')")
        #
        # con.commit()





    # BustlePCFG.initialize(operations=dsl_functions, string_literals=string_literals,
    #                       integer_literals=integer_literals, boolean_literals=[True, False],
    #                       string_variables=string_variables, integer_variables=integer_variables)



if __name__ == '__main__':
    main()

