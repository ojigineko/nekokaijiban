require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');

const supabaseUrl = process.env.SUPABASE_URL;
const supabaseKey = process.env.SUPABASE_ANON_KEY;

const supabase = createClient(supabaseUrl, supabaseKey);

async function testConnection() {
  try {
    const { data, error } = await supabase.from('your_table').select('*').limit(1);
    
    if (error) {
      console.error('接続エラー:', error.message);
      return;
    }
    
    console.log('Supabaseに正常に接続されました！');
    console.log('データのサンプル:', data);
  } catch (err) {
    console.error('予期せぬエラーが発生しました:', err.message);
  }
}

testConnection(); 