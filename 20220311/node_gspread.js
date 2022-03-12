const {GoogleSpreadsheet} = require('google-spreadsheet');
const jsonfile =  JSON.parse(fs.readFileSync('./gspread.json', 'utf8'));
const spreadsheet_key = ""
async () =>{
    const gs = new GoogleSpreadsheet(spreadsheet_key);
    
    await gs.useServiceAccountAuth({
      client_email: jsonfile.client_email,
      private_key: jsonfile.private_key,
    });
    console.log("スプレッドシート接続");
    await gs.loadInfo();
    const sheet1 = await gs.sheetsById[0];
    const rows = await sheet1.getRows();
    console.log(rows);

}