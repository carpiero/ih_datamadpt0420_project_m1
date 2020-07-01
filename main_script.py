import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Set country')
    parser.add_argument("-c", "--country", help="specify country for the results", type=str)
    parser.add_argument("-p" , "--path" , help="specify the path of the database, the file .db" , type=str,required=True)
    parser.add_argument("-u" , "--unemployed" , help="specify the results with Unemployed or Part time Job or Inactive effect, must be yes or no, default=yes" , type=str)
    args = parser.parse_args()
    return args

def main(arguments):

    data = mac.acquire(arguments.path)
    filtered = mwr.wrangle(data , arguments.unemployed)
    results = man.analyze(filtered)
    results.to_csv('./data/results/df_results.csv')

    reporting = mre.reporting(results, arguments.country)

    print(reporting)

    print('\n\n========================= Pipeline is complete. You may find the results in the folder ./data/results =========================\n\n')


if __name__ == '__main__':

    try:
        arguments = argument_parser()
        main(arguments)

    except TypeError:

        print('\n=================================================================================================\n\nERROR: Please insert a Yes or No for Unemployed argument. \n\n=================================================================================================\n\n')

    except NameError:

        print('\n=================================================================================================\n\nERROR: Please insert a correct Country of the list inside ./data/results/country_list.csv\n\n=================================================================================================\n\n')


