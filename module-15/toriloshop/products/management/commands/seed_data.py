# products/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User  # Import User
from products.models import Category, Product


class Command(BaseCommand):
    help = 'Seeds the database with sample categories and products'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write('  Cleared existing data')

        # NEW: Get or create a default admin user for seeding
        # This ensures seeded products have a created_by value
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@toriloshop.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write('  Created default admin user (username: admin, password: admin123)')
        else:
            self.stdout.write('  Using existing admin user')
        
        # ============================================
        # CREATE CATEGORIES
        # ============================================
        categories_data = [
            {
                'name': 'Electronics',
                'description': 'Smartphones, laptops, tablets, headphones, and tech accessories'
            },
            {
                'name': 'Clothing',
                'description': "Men's and women's apparel, footwear, and fashion accessories"
            },
            {
                'name': 'Books',
                'description': 'Fiction, non-fiction, educational books, and programming guides'
            },
            {
                'name': 'Home & Garden',
                'description': 'Furniture, home decor, smart home devices, and gardening supplies'
            },
            {
                'name': 'Sports',
                'description': 'Fitness equipment, sportswear, and outdoor gear'
            },
            {
                'name': 'Toys & Games',
                'description': 'Board games, video games, building sets, and educational toys'
            },
        ]
        
        categories = {}
        for cat_data in categories_data:
            category = Category.objects.create(
                name=cat_data['name'],
                description=cat_data['description']
            )
            categories[cat_data['name']] = category
            self.stdout.write(f'  ✓ Created category: {category.name}')
        
        self.stdout.write('')
        
        # ============================================
        # CREATE PRODUCTS
        # Images are intentionally left blank — upload via admin or product edit form
        # ============================================
        products_data = [
            # ------------------------------------------
            # Electronics
            # ------------------------------------------
            {
                'name': 'iPhone 15 Pro',
                'category': 'Electronics',
                'price': 1499.99,
                'stock': 15,
                'description': (
                    'Apple iPhone 15 Pro with A17 Pro chip, 6.1-inch Super Retina XDR display, '
                    '48MP main camera, titanium design, and USB-C. Available in Natural Titanium.'
                )
            },
            {
                'name': 'Samsung Galaxy S24 Ultra',
                'category': 'Electronics',
                'price': 1299.99,
                'stock': 20,
                'description': (
                    'Samsung Galaxy S24 Ultra with Galaxy AI, 6.8-inch Dynamic AMOLED 2X display, '
                    '200MP camera, S Pen included, and 5000mAh battery.'
                )
            },
            {
                'name': 'MacBook Air M2',
                'category': 'Electronics',
                'price': 1199.99,
                'stock': 10,
                'description': (
                    'Apple MacBook Air with M2 chip, 13.6-inch Liquid Retina display, '
                    '8GB RAM, 256GB SSD, and up to 18 hours of battery life. Stunningly thin design.'
                )
            },
            {
                'name': 'Sony WH-1000XM5',
                'category': 'Electronics',
                'price': 349.99,
                'stock': 25,
                'description': (
                    'Industry-leading noise cancelling wireless headphones with 30-hour battery, '
                    'crystal clear hands-free calling, and multipoint connection.'
                )
            },
            {
                'name': 'iPad Pro 12.9" M2',
                'category': 'Electronics',
                'price': 1099.99,
                'stock': 8,
                'description': (
                    '12.9-inch iPad Pro with M2 chip, Liquid Retina XDR display, '
                    'Apple Pencil hover support, and Thunderbolt port. Ultimate creative tool.'
                )
            },
            {
                'name': 'Dell UltraSharp 27" 4K Monitor',
                'category': 'Electronics',
                'price': 549.99,
                'stock': 12,
                'description': (
                    '27-inch 4K UHD IPS monitor with 99% sRGB, USB-C connectivity, '
                    'built-in speakers, and adjustable stand. Perfect for creative professionals.'
                )
            },
            {
                'name': 'Logitech MX Master 3S Mouse',
                'category': 'Electronics',
                'price': 99.99,
                'stock': 35,
                'description': (
                    'Premium wireless mouse with 8K DPI, MagSpeed electromagnetic scrolling, '
                    'USB-C charging, and ergonomic design. Works on any surface including glass.'
                )
            },
            {
                'name': 'Razer BlackWidow V4 Pro Keyboard',
                'category': 'Electronics',
                'price': 229.99,
                'stock': 14,
                'description': (
                    'Mechanical gaming keyboard with Razer Green switches, programmable command dial, '
                    'plush leatherette wrist rest, and per-key RGB lighting.'
                )
            },
            {
                'name': 'Fujifilm X-T5 Mirrorless Camera',
                'category': 'Electronics',
                'price': 1699.99,
                'stock': 5,
                'description': (
                    '40MP APS-C mirrorless camera with 5-axis in-body stabilisation, '
                    'film simulation modes, and tilting LCD screen. Perfect for photography enthusiasts.'
                )
            },
            {
                'name': 'Samsung Galaxy Tab S9',
                'category': 'Electronics',
                'price': 799.99,
                'stock': 0,  # Out of stock
                'description': (
                    '11-inch Dynamic AMOLED 2X tablet with S Pen, IP68 water resistance, '
                    'Snapdragon 8 Gen 2 processor, and quad speakers tuned by AKG.'
                )
            },
            
            # ------------------------------------------
            # Clothing
            # ------------------------------------------
            {
                'name': "Levi's 501 Original Fit Jeans",
                'category': 'Clothing',
                'price': 69.99,
                'stock': 50,
                'description': (
                    "Iconic straight-fit jeans in premium denim. Features Levi's signature button fly "
                    "and riveted construction. A timeless classic since 1873."
                )
            },
            {
                'name': 'Nike Air Max 270 React',
                'category': 'Clothing',
                'price': 149.99,
                'stock': 30,
                'description': (
                    'Lifestyle sneaker combining a 270 Max Air unit with React foam midsole. '
                    'Breathable mesh upper with seamless overlays for modern style.'
                )
            },
            {
                'name': 'Adidas Ultraboost Light',
                'category': 'Clothing',
                'price': 189.99,
                'stock': 25,
                'description': (
                    'Revolutionary running shoe with Light BOOST cushioning — 30% lighter than previous '
                    'generations. Primeknit+ upper adapts to foot movement for locked-in fit.'
                )
            },
            {
                'name': 'The North Face Arctic Parka',
                'category': 'Clothing',
                'price': 349.99,
                'stock': 12,
                'description': (
                    'Waterproof, windproof, and insulated parka rated to -25°C. Features 550-fill goose down, '
                    'removable faux-fur hood trim, and multiple secure-zip pockets.'
                )
            },
            {
                'name': 'Uniqlo Supima Cotton Crew Neck T-Shirt',
                'category': 'Clothing',
                'price': 19.90,
                'stock': 100,
                'description': (
                    'Premium Supima cotton t-shirt with a smooth, soft feel. Classic fit with reinforced '
                    'neck ribbing. Available in multiple colours.'
                )
            },
            {
                'name': 'Patagonia Better Sweater Fleece',
                'category': 'Clothing',
                'price': 139.00,
                'stock': 22,
                'description': (
                    'Fair Trade Certified fleece jacket made from 100% recycled polyester. '
                    'Features dyed-to-match zippers and zippered chest pocket. Bluesign approved.'
                )
            },
            {
                'name': 'Ray-Ban Aviator Classic',
                'category': 'Clothing',
                'price': 163.00,
                'stock': 18,
                'description': (
                    'Timeless aviator sunglasses with G-15 non-polarized lenses, gold metal frame, '
                    'and 100% UV protection. Worn by pilots since 1937.'
                )
            },
            
            # ------------------------------------------
            # Books
            # ------------------------------------------
            {
                'name': 'Clean Code: A Handbook of Agile Software Craftsmanship',
                'category': 'Books',
                'price': 39.99,
                'stock': 20,
                'description': (
                    'Robert C. Martin\'s definitive guide to writing clean, readable, maintainable code. '
                    'Covers meaningful naming, function design, error handling, and test-driven development. '
                    'A must-read for every software developer.'
                )
            },
            {
                'name': 'The Pragmatic Programmer: Your Journey to Mastery',
                'category': 'Books',
                'price': 49.99,
                'stock': 15,
                'description': (
                    'David Thomas and Andrew Hunt\'s classic guide is newly revised for the modern era. '
                    'Learn practical approaches to software development — from personal responsibility '
                    'to architectural design to team collaboration.'
                )
            },
            {
                'name': 'Atomic Habits: An Easy & Proven Way to Build Good Habits',
                'category': 'Books',
                'price': 16.99,
                'stock': 35,
                'description': (
                    'James Clear reveals how atomic changes can yield remarkable results. '
                    'No matter your goals, Atomic Habits offers a proven framework for improving every day. '
                    'Over 15 million copies sold worldwide.'
                )
            },
            {
                'name': 'Deep Work: Rules for Focused Success in a Distracted World',
                'category': 'Books',
                'price': 14.99,
                'stock': 0,  # Out of stock
                'description': (
                    'Cal Newport explains how the ability to focus without distraction is becoming '
                    'increasingly rare and valuable. Includes actionable advice for cultivating a deep work ethic.'
                )
            },
            {
                'name': 'Python Crash Course (3rd Edition)',
                'category': 'Books',
                'price': 34.99,
                'stock': 28,
                'description': (
                    'Eric Matthes\'s hands-on, project-based introduction to Python. Build games, '
                    'data visualisations, and web applications as you learn. Covers Python 3.x with '
                    'Django, matplotlib, and Plotly.'
                )
            },
            {
                'name': 'Designing Data-Intensive Applications',
                'category': 'Books',
                'price': 44.99,
                'stock': 12,
                'description': (
                    'Martin Kleppmann explores the fundamental ideas behind reliable, scalable, '
                    'and maintainable data systems. Covers databases, streaming, batch processing, '
                    'and distributed systems.'
                )
            },
            {
                'name': 'The Lean Startup',
                'category': 'Books',
                'price': 12.99,
                'stock': 40,
                'description': (
                    'Eric Ries defines a scientific approach to creating and managing successful startups. '
                    'Learn about validated learning, build-measure-learn feedback loops, and innovation accounting.'
                )
            },
            
            # ------------------------------------------
            # Home & Garden
            # ------------------------------------------
            {
                'name': 'IKEA BEKANT Standing Desk',
                'category': 'Home & Garden',
                'price': 449.00,
                'stock': 8,
                'description': (
                    'Sit/stand desk with electric height adjustment from 65cm to 125cm. '
                    '160×80cm desk surface in white/black. Cable management net included.'
                )
            },
            {
                'name': 'Herman Miller Aeron Chair',
                'category': 'Home & Garden',
                'price': 1395.00,
                'stock': 5,
                'description': (
                    'Iconic ergonomic office chair with PostureFit SL back support, 8Z Pellicle suspension, '
                    'and fully adjustable arms. Designed for 24/7 use. 12-year warranty included.'
                )
            },
            {
                'name': 'Philips Hue Starter Kit',
                'category': 'Home & Garden',
                'price': 199.99,
                'stock': 18,
                'description': (
                    'Smart lighting system with 3 colour-changing bulbs, Hue Bridge, and smart control via '
                    'app or voice. Compatible with Alexa, Google Assistant, and Apple HomeKit.'
                )
            },
            {
                'name': 'Monstera Deliciosa Indoor Plant',
                'category': 'Home & Garden',
                'price': 34.99,
                'stock': 25,
                'description': (
                    'Beautiful Swiss cheese plant in a 21cm nursery pot. Easy-care tropical plant that '
                    'thrives in indirect light. Perfect for adding greenery to any room.'
                )
            },
            {
                'name': 'Nest Learning Thermostat (4th Gen)',
                'category': 'Home & Garden',
                'price': 249.99,
                'stock': 10,
                'description': (
                    'Smart thermostat that learns your schedule and programs itself. Energy-saving Eco mode, '
                    'remote control via app, and sleek stainless steel design.'
                )
            },
            {
                'name': 'Dyson V15 Detect Cordless Vacuum',
                'category': 'Home & Garden',
                'price': 749.99,
                'stock': 7,
                'description': (
                    'Cordless stick vacuum with laser dust detection, piezo sensor for particle counting, '
                    '60-minute runtime, and advanced whole-machine HEPA filtration.'
                )
            },
            
            # ------------------------------------------
            # Sports
            # ------------------------------------------
            {
                'name': 'Manduka PRO Yoga Mat',
                'category': 'Sports',
                'price': 120.00,
                'stock': 30,
                'description': (
                    'Professional 6mm yoga mat with closed-cell surface to prevent sweat absorption. '
                    'Lifetime guarantee. 182cm × 66cm, 3.4kg. Used by yoga teachers worldwide.'
                )
            },
            {
                'name': 'Bowflex SelectTech 552 Dumbbells',
                'category': 'Sports',
                'price': 429.00,
                'stock': 12,
                'description': (
                    'Adjustable dumbbell set replacing 15 sets of weights. Adjusts from 2.5kg to 24kg '
                    'with a dial turn. Compact design saves space in your home gym.'
                )
            },
            {
                'name': 'Spalding NBA Official Game Ball',
                'category': 'Sports',
                'price': 169.99,
                'stock': 22,
                'description': (
                    'Official NBA game basketball made from genuine leather. Size 7 (29.5"). '
                    'Composite microfibre internal construction for superior grip and durability.'
                )
            },
            {
                'name': 'Wilson Pro Staff RF97 Tennis Racket',
                'category': 'Sports',
                'price': 249.00,
                'stock': 10,
                'description': (
                    'Roger Federer signature frame with braided graphite composition, 340g unstrung weight, '
                    'and head size of 97 sq. inches. Precision and feel for advanced players.'
                )
            },
            {
                'name': 'Garmin Forerunner 265 Running Watch',
                'category': 'Sports',
                'price': 449.99,
                'stock': 15,
                'description': (
                    'GPS running watch with AMOLED touchscreen display, training readiness score, '
                    'morning report, wrist-based running power, and up to 13 days of battery life.'
                )
            },
            {
                'name': 'Coleman Sundome 4-Person Tent',
                'category': 'Sports',
                'price': 99.99,
                'stock': 18,
                'description': (
                    'Spacious dome tent that fits 4 people. Features WeatherTec system with patented '
                    'welded floors, inverted seams, and Insta-Clip pole attachments. Setup in 10 minutes.'
                )
            },
            
            # ------------------------------------------
            # Toys & Games
            # ------------------------------------------
            {
                'name': 'LEGO Star Wars Millennium Falcon',
                'category': 'Toys & Games',
                'price': 159.99,
                'stock': 18,
                'description': (
                    '1,351-piece LEGO Star Wars set featuring the iconic Millennium Falcon. '
                    'Includes Han Solo, Chewbacca, Finn, and BB-8 minifigures. Perfect for ages 9+.'
                )
            },
            {
                'name': 'Nintendo Switch OLED - Mario Red Edition',
                'category': 'Toys & Games',
                'price': 349.99,
                'stock': 10,
                'description': (
                    'Nintendo Switch with vibrant 7-inch OLED screen, wide adjustable stand, '
                    '64GB internal storage, and enhanced audio. Includes Mario-themed red Joy-Con and dock.'
                )
            },
            {
                'name': 'Catan (Settlers of Catan) Board Game',
                'category': 'Toys & Games',
                'price': 44.99,
                'stock': 30,
                'description': (
                    'Award-winning strategy board game for 3-4 players. Collect resources, build settlements, '
                    'and trade your way to victory on the ever-changing island of Catan. Ages 10+.'
                )
            },
            {
                'name': 'PlayStation 5 Console (Slim)',
                'category': 'Toys & Games',
                'price': 499.99,
                'stock': 5,
                'description': (
                    'PS5 Slim with 1TB SSD, haptic feedback controllers, ray tracing, '
                    'and 3D audio. Smaller design with detachable disc drive option.'
                )
            },
            {
                'name': 'Ravensburger 1000-Piece Jigsaw Puzzle',
                'category': 'Toys & Games',
                'price': 19.99,
                'stock': 35,
                'description': (
                    'Premium 1000-piece puzzle with softclick technology for perfect interlocking. '
                    'Vibrant colours and matte finish. Finished size: 70cm × 50cm. Ages 12+.'
                )
            },
        ]
        
        # Create all products
        for prod_data in products_data:
            product = Product.objects.create(
                name=prod_data['name'],
                category=categories[prod_data['category']],
                price=prod_data['price'],
                stock=prod_data['stock'],
                description=prod_data['description'],
                created_by=admin_user,  # NEW: Assign creator
                created_at=timezone.now()
                # image is not set — upload via admin panel or product edit form
            )
            
            # Show stock status in output
            stock_status = '✓ In Stock' if product.stock > 0 else '✗ Out of Stock'
            self.stdout.write(
                f'  {stock_status} | {product.name} '
                f'({product.category.name}) — ₦{product.price:,.2f}'
            )
        
        # Summary
        total_categories = Category.objects.count()
        total_products = Product.objects.count()
        in_stock = Product.objects.filter(stock__gt=0).count()
        out_of_stock = Product.objects.filter(stock=0).count()
        
        self.stdout.write('')
        self.stdout.write('=' * 60)
        self.stdout.write(
            self.style.SUCCESS(
                f'✓ Database seeded successfully!'
            )
        )
        self.stdout.write(f'  Categories: {total_categories}')
        self.stdout.write(f'  Total Products: {total_products}')
        self.stdout.write(f'  In Stock: {in_stock}')
        self.stdout.write(f'  Out of Stock: {out_of_stock}')
        self.stdout.write('')
        self.stdout.write('  ℹ Product images are not set — upload via admin panel')
        self.stdout.write('    Admin URL: http://127.0.0.1:8000/admin/')
        self.stdout.write('=' * 60)