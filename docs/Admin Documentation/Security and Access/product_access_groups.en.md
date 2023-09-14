# Product Access Groups

!!! info "This feature is not enabled by default"
    If you want to try out product access groups for your organization, please reach out to <asm-support.df@asmpt.com>.

Service organizations often have different teams which need to access different types of documents. Service sales will need price lists and product brochures, technicians on the field will need service manuals and technical bulletins, commissioning teams will need assembly instructions, etc.

Simply put, **users will only be able to see product lines (and their corresponding documents and content units) that are assigned to the product access group they belong to.**

![Status Quo](https://i.imgur.com/VnLylKq.png)


If you want to **restrict access** to certain information only to parts of your service organization, then product access groups are for you. **Product Access Groups are not activated by default.**

If you are interested in more details about product access groups, see the example below.

??? example

    Imagine a company, **3D Printers GmbH**. They produce and market 3D printers for the industrial market. They are using ASMPT Virtual Assist for their extensive documentation and information delivery needs. 3D Printers GmbH has two divisions based on their region: **EMEA** and **Americas**. Both of these divisions are under **Global Management**, headquartered in Munich.

    Chandler is a global service manager and is in charge of coordinating all service operations across the world. Joey and Ross, the heads of service for EMEA and Americas, respectively, report to him.

    There are two types of documents Chandler wants to make accessible through ASMPT Virtual Assist:

    - 3D Printers (assembly instructions, circuit diagrams, service manuals, etc.)
    - Sales documents (brochures, price lists, catalogs)

    ### Problem 
    Sales documents vary across regions: European businesses are charged more than South American ones due to the cost of labor. The 3D printers themselves, however, are identical everywhere.

    ### Solution
    In order to avoid confusing the service teams for each region, Chandler decides to split the sales documents into **Sales Documents (EMEA)** and **Sales Documents (Americas)**. 

    He still wants all users to have access to the 3D printer documentation but wants to restrict access to the sales documents based on region.

    Here's where **Product Access Groups** can help: with ASMPT Virtual Assist's help, Chandler creates three different access groups:

    - **Global product group** for Chandler and his team in Munich
    - **EMEA product group** for everyone in the EMEA team
    - **Americas product group** for everyone in the Americas team

    ![Status Quo](https://i.imgur.com/xq4Lbn4.png)

    ### What does this mean?

    Quite simply, users will only be able to see product lines that are assigned to the product access group they belong to.

    For Joey, head of service for EMEA, it looks like this:

    ![Head of Service EMEA](https://i.imgur.com/B7JMtGo.png)

    Joey can see two product lines, the ones which are relevant to his work.

    Chandler can see all product lines since all product lines belong to the Global product group.

    ![Global Head of Service](https://i.imgur.com/L4rfLfc.png)
