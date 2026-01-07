<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class PageController extends AbstractController
{
    #[Route('/', name: 'app_home')]
    public function home(): Response
    {
        $reportPath = $this->getParameter('kernel.project_dir') . '/Network_Report.md';
        $reportContent = "Le rapport n'a pas encore été généré. Cliquez sur le bouton ci-dessus.";

        if (file_exists($reportPath)) {
            $reportContent = file_get_contents($reportPath);
        }

        return $this->render('home/index.html.twig', [
            'reportContent' => $reportContent
        ]);
    }

    #[Route('/run-python', name: 'run_python')]
    public function runPython(): Response
    {
        $projectRoot = $this->getParameter('kernel.project_dir');
        
        // Exécution des deux scripts l'un après l'autre
        $command = "python $projectRoot/scripts/txt_to_csv.py && python $projectRoot/scripts/csv_to_md.py";
        shell_exec($command);

        $this->addFlash('success', 'Analyse terminée ! Le rapport a été mis à jour.');
        return $this->redirectToRoute('app_home');
    }
}