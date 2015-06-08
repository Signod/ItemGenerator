import csv





















#################################################################################################
#                                                                                               #
# Generator Functions Here                                                                      # 
#                                                                                               #
#################################################################################################

    def Generated_Item_Writer(Name, *args)
        with open(Name, 'wb') as csvfile:
            ItemWriter = csv.writer(csvfile, delimiter='', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            ItemWriter.writenow([Name]+][*args])
        