using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.Net;
using System.IO;

namespace TypewriteUtil
{
    public class ImageUtil
    {
        public static  Bitmap GetImage(Uri url)
        {
            var wc = new WebClient();
            var data = wc.DownloadData(url);
            var bm = Bitmap.FromStream(new MemoryStream(data)) as Bitmap;
            
            return bm;
        }

        public static Image GetImage(string path)
        {
            var fs = File.Open(path, FileMode.Open);
            return Bitmap.FromStream(fs);
        }

        public static Bitmap ResizeImage(Bitmap img, int height, int width)
        {
            return new Bitmap(img, new Size(width, height));
        }

        public static Color[] GetImageAsColorArray(Image img)
        {
            var ic = new ImageConverter();
            Color[] pixels = (Color[])ic.ConvertTo(img, typeof(Color[]));

            return pixels;
        }
    }
}
